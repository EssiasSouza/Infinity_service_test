
# Prevent Screen Lock Script

Este script foi desenvolvido para impedir o bloqueio da tela, simulando a pressão de uma tecla em intervalos regulares. Isso é útil em situações onde você precisa manter a tela ativa sem intervenção manual, como durante apresentações, monitoramento de sistemas, ou outras atividades que exigem a tela desbloqueada.

## Como Funciona

O script utiliza a biblioteca `pyautogui` para simular a pressão da tecla `Shift` a cada 60 segundos. Ao pressionar repetidamente a tecla `Shift`, o sistema entende que há atividade contínua, evitando assim o bloqueio da tela.

## Pré-requisitos

- Python 3.x
- Biblioteca `pyautogui`

## Instalação

Antes de executar o script, certifique-se de ter a biblioteca `pyautogui` instalada. Você pode instalá-la usando o `pip`:

```bash
pip install pyautogui
```

## Uso

Para executar o script, basta rodar o seguinte comando no terminal:

```bash
python your_script_name.py
```

Substitua `your_script_name.py` pelo nome do arquivo que contém o script.

## Script

Aqui está o código completo do script:

```python
import pyautogui
import time

pyautogui.FAILSAFE = False

def enchamba():
    while True:
        pyautogui.press('shift')
        time.sleep(60)

if __name__ == "__main__":
    enchamba()
```

## Explicação do Código

- **pyautogui.FAILSAFE = False**: Desativa a função de segurança do `pyautogui` que interrompe o script quando o mouse é movido para o canto superior esquerdo da tela.
- **def enchamba()**: Define uma função chamada `enchamba` que contém um loop infinito.
- **while True**: Inicia um loop que nunca termina, mantendo o script em execução contínua.
- **pyautogui.press('shift')**: Simula a pressão da tecla `Shift`.
- **time.sleep(60)**: Pausa a execução do script por 60 segundos antes de repetir a pressão da tecla `Shift`.

## Considerações

- Use este script com cuidado, especialmente em ambientes de produção, pois ele impede o bloqueio da tela, o que pode ter implicações de segurança.
- Certifique-se de que você compreende os riscos e responsabilidades de manter uma tela desbloqueada.

## Contribuição

Se você deseja contribuir com melhorias para este script, sinta-se à vontade para enviar um pull request.

## Contato

Para dúvidas ou sugestões, entre em contato comigo:

- Nome: Essias Souza
- LinkedIn: [Essias Souza](https://www.linkedin.com/in/essias/1)
- GitHub: [essias](https://github.com/EssiasSouza)

---

Este é um projeto simples, mas útil para manter a tela do seu computador ativa. Espero que seja útil para você!
