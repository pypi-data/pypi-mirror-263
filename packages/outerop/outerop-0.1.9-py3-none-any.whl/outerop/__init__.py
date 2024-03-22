import json
import time
from typing import List, Dict, Union
import requests
from openai import OpenAI
from anthropic import Anthropic
from mistralai.client import MistralClient

class LogCollector:
    def __init__(self, config: Dict):
        self.config = {**{"isEnabled": True, "baseURL": "https://app.outerop.com"}, **config}
        self.outerop_api_key = config["outeropApiKey"]
        self.pending_flush = False
        self.buffer = []

    @property
    def is_enabled(self):
        return self.config["isEnabled"]

    def record(self, event: Dict):
        prepared_event = self._prepare_event(event)
        self.buffer.append(prepared_event)
        self.flush()

    def flush(self):
        try:
            response = requests.post(
                f"{self.config['baseURL']}/api/v1/log",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": self.outerop_api_key,
                },
                data=json.dumps(self.buffer),
            )
            response.raise_for_status()
        except requests.exceptions.RequestException:
            pass
        finally:
            self.pending_flush = False
            self.buffer = []

    def _prepare_event(self, event: Dict):
        return {**event}


class Outerop:
    def __init__(self, outerop_api_key: str, options: Dict = None):
        self.outerop_api_key = outerop_api_key
        self.options = {**{"baseURL": "https://app.outerop.com", "loggingEnabled": True}, **(options or {})}

        self.log_collector = LogCollector(
            {
                "isEnabled": True,
                "baseURL": self.options.get("baseURL", "https://app.outerop.com"),
                "outeropApiKey": self.outerop_api_key,
            }
        )

        headers = {
            "Authorization": self.outerop_api_key,
            "Content-Type": "application/json",
        }
        if self.options.get("bypassHeader"):
            headers["x-vercel-protection-bypass"] = self.options["bypassHeader"]

        self.client = requests.Session()
        self.client.headers.update(headers)
        self.client.base_url = self.options["baseURL"]

        self.openai = None
        if self.options.get("openaiApiKey"):
            self.openai = OpenAI(api_key=self.options["openaiApiKey"])

        self.anthropic = None
        if self.options.get("anthropicApiKey"):
            self.anthropic = Anthropic(api_key=self.options["anthropicApiKey"])

        self.mistral = None
        if self.options.get("mistralApiKey"):
            self.mistral = MistralClient(api_key=self.options["mistralApiKey"])

        self.prompt_cache: Dict[str, Dict] = {}

    def get_prompt(self, prompt_uuid: str, environment: str, version: Union[int, str]):
        cache_key = f"{prompt_uuid}-{environment}-{version}"
        if cache_key in self.prompt_cache:
            return self.prompt_cache[cache_key]

        try:
            print(f"promptUuid: {prompt_uuid}")
            print(f"environment: {environment}")
            print(f"version: {version}")
            print(f"api key: {self.outerop_api_key}")

            url = f"{self.options['baseURL']}/api/v1/prompt/{prompt_uuid}/{environment}/{version}"
            response = self.client.get(url)
            response.raise_for_status()
            self.prompt_cache[cache_key] = response.json()["prompt"]
            return response.json()["prompt"]
        except requests.exceptions.RequestException as e:
            status_code = e.response.status_code if e.response else "Unknown"
            response_text = e.response.text if e.response else "Unknown"
            raise Exception(f"Request failed with status code {status_code}: {response_text}")
        except Exception as e:
            print(f"error: {e}")
            raise Exception(f"Request failed: {e}")
        

    def chat(
        self,
        prompt_uuid: str,
        environment: str,
        version: Union[int, str],
        variables: Dict[str, str],
        name: str = None,
    ):
        prompt = self.get_prompt(prompt_uuid, environment, version)
        messages = replace_variables_in_prompts(prompt["messages"], variables)
        messages_without_id = [
            {k: v for k, v in message.items() if k != "id"} for message in messages
        ]

        try:
            tools = prompt["tools"] if prompt["tools"] and len(prompt["tools"]) > 0 else None

            print(prompt)

            if prompt["model_config"]["provider"] == "mistral":
                if not self.mistral:
                    raise Exception("Mistral API key is not provided")

                start_time = time.perf_counter()
                result = self.mistral.chat(
                    messages=messages_without_id,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    tools=tools,
                    tool_choice=prompt.get("tool_choice", "auto"),
                )
                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)

                print(f"result: {result}")

                self.log_collector.record(
                    {
                        "version": prompt["version"],
                        "team_prompt_id": prompt["team_prompt_id"],
                        "environment": prompt["environment"],
                        "prompt_environment_id": prompt["id"],
                        "input": messages_without_id,
                        "output": result.choices[0].message.content,
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage.completion_tokens,
                        "input_tokens": result.usage.prompt_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )
                return result

            if prompt["model_config"]["provider"] == "openai":
                if not self.openai:
                    raise Exception("OpenAI API key is not provided")

                start_time = time.perf_counter()
                result = self.openai.chat.completions.create(
                    messages=messages_without_id,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    tools=tools,
                    tool_choice=prompt.get("tool_choice", "auto"),
                )
                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)

                print(f"result: {result}")

                self.log_collector.record(
                    {
                        "version": prompt["version"],
                        "team_prompt_id": prompt["team_prompt_id"],
                        "environment": prompt["environment"],
                        "prompt_environment_id": prompt["id"],
                        "input": messages_without_id,
                        "output": result.choices[0].message.content,
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage.completion_tokens,
                        "input_tokens": result.usage.prompt_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )
                return result

            if prompt["model_config"]["provider"] == "anthropic":
                if not self.anthropic:
                    raise Exception("Anthropic API key is not provided")

                if prompt.get("tool_choice") or prompt.get("tools"):
                    raise Exception("Anthropic tools are not supported yet")

                start_time = time.perf_counter()

                # Extract and combine system prompts in messages into one long string
                system_prompt = "\n".join(
                    [message["content"] for message in messages if message["role"] == "system"]
                )

                # Filter out system messages from the messages list and ensure each message has a 'role' field
                messages_without_system = [
                    {"role": message["role"], "content": message["content"]}
                    for message in messages
                    if message["role"] != "system"
                ]

                result = self.anthropic.messages.create(
                    messages=messages_without_system,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    system=system_prompt,
                )

                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)

                self.log_collector.record(
                    {
                        "version": prompt["version"],
                        "team_prompt_id": prompt["team_prompt_id"],
                        "prompt_environment_id": prompt["id"],
                        "environment": prompt["environment"],
                        "input": messages_without_id,
                        "output": result.completion,
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage_info.completion_tokens,
                        "input_tokens": result.usage_info.prompt_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )

                return result

        except Exception as e:
            raise Exception(f"Request failed: {e}")

    def ping(self):
        try:
            url = f"{self.options['baseURL']}/ping"
            response = self.client.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            status_code = e.response.status_code if e.response else "Unknown"
            response_text = e.response.text if e.response else "Unknown"
            raise Exception(f"Request failed with status code {status_code}: {response_text}")
        except Exception as e:
            raise Exception(f"Request failed: {e}")

def extract_variables(content: str) -> List[str]:
    import re

    return [v.replace("{{", "").replace("}}", "").strip() for v in re.findall(r"{{(.*?)}}", content)]


def replace_variables(content: str, variables: Dict[str, str]) -> str:
    for variable_name, value in variables.items():
        content = content.replace(f"{{{{{ variable_name }}}}}", value)
    return content


def replace_variables_in_prompts(
    prompts: List[Dict], variables: Dict[str, str]
) -> List[Dict]:
    return [
        {**prompt, "content": replace_variables(prompt["content"], variables)} for prompt in prompts
    ]