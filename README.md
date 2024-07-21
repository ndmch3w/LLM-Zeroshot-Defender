# Instructions

## Setup
- Install Ollama: https://ollama.com/download
- Find LLMs on Ollama's library: https://ollama.com/library (currently, the project has been tested with llama2:7b-chat-q8_0, llama2:13b-chat-q4_0, llama2:13b-chat-q8_0)
- Install a LLM: ollama run <model_name>
- Check installed LLM: ollama list

## How to run?

### Initiate harm filter
Run harm filter: ollama run <model_name>

### Test with original dataset
- Replace corresponding parameters with the path of targeted responses file (responses samples from dataset) and results file (indications from harm filter) & Run /filter/new_filter.py
![image](https://github.com/user-attachments/assets/adcad4cc-171a-43c2-b09b-db652974af90)
- Replace corresponding parameters with the path of targeted responses file (responses samples from dataset) and results file (indications from harm filter) & Run /utils/compare.py
![image](https://github.com/user-attachments/assets/28683d9e-8eec-4f49-a98a-696e83c3e93d)

### Test with GPTFuzzer examples
- If the GPTFuzzer's dataset has not been modified to same format with original dataset: Replace corresponding paramater with the path of GPTFuzzer's example responses file & Run /utils/data_modifier.py
![image](https://github.com/user-attachments/assets/52cf0ca0-329c-434b-9290-b37df493a421)
- Replace corresponding parameters with the path of targeted responses file (responses samples from GPTFuzzer's dataset) and results file (indications from harm filter) & Run /filter/new_filter.py
![image](https://github.com/user-attachments/assets/adcad4cc-171a-43c2-b09b-db652974af90)
- Replace corresponding parameters with the path of targeted responses file (responses samples from dataset) and results file (indications from harm filter) & Run /utils/compare.py
![image](https://github.com/user-attachments/assets/28683d9e-8eec-4f49-a98a-696e83c3e93d)
