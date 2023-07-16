# ADB, Python e Instagram: Automatização de Postagens

## Pacotes:

###  pip install adbkit adb-push-create==0.11

 https://github.com/hansalemaos/adbkit
 
### Instale Instagram lite:

https://play.google.com/store/apps/details?id=com.instagram.lite&hl=pt_BR

### Instale Python 3.10
 
[![YT](https://i.ytimg.com/vi/WqXMQEYfDfM/maxresdefault.jpg)](https://www.youtube.com/watch?v=WqXMQEYfDfM)
[https://www.youtube.com/watch?v=WqXMQEYfDfM]()

Neste vídeo, demonstro como automatizar o processo de postagem de imagens e legendas no Instagram usando Python e ADBKit. ADBKit é uma biblioteca Python que nos permite interagir com dispositivos Android através da Android Debug Bridge (ADB). Com esse script de automação, você pode agendar e fazer postagens em sua conta do Instagram automaticamente.

Descrição do Código:

O código Python fornecido automatiza o processo de postagem usando o ADBKit e algumas bibliotecas adicionais. Aqui está uma explicação detalhada do código:

Importando Bibliotecas:
As bibliotecas necessárias são importadas, incluindo os, pandas, ADBTools do ADBKit e sleep do módulo time.

Função para Obter o Quadro do UI Automator:
Essa função recupera a hierarquia atual da interface do usuário (UI) do dispositivo Android conectado usando o ADBKit. Ela procura por elementos exibidos na UI e retorna os dados relevantes em um DataFrame do pandas.

Conectando ao Dispositivo:
O código estabelece uma conexão com o dispositivo Android usando o ADB. Certifique-se de especificar o caminho correto para o binário adb.exe e o número de série do dispositivo.

Enviando a Imagem para o Dispositivo:
O código encontra a imagem mais recente em uma pasta específica (C:\instaposts\) e a envia para a pasta /sdcard/DCIM/ do dispositivo Android.

Acionando a Verificação de Mídia:
O script envia um broadcast de intenção para acionar a Verificação de Mídia no dispositivo, para que ele fique ciente da nova imagem adicionada.

Abrindo o Instagram Lite:
O código inicia o aplicativo Instagram Lite usando um comando de shell do ADB.

Interagindo com Elementos da Interface de Usuário (UI):
O script interage com os elementos da interface do usuário do Instagram usando as coordenadas e o conteúdo do texto encontrados no quadro do UI Automator. Ele realiza várias ações, como tocar na tela, digitar texto e muito mais, para fazer a postagem da imagem e da legenda.

Observação: Este código foi projetado para funcionar com elementos específicos da interface do usuário em uma versão específica do aplicativo Instagram Lite. Mudanças na estrutura do aplicativo ou atualizações podem exigir ajustes no código.

Para uma explicação mais detalhada e uma demonstração completa, assista ao vídeo. Espero que este tutorial seja útil para automatizar o processo de postagem no Instagram usando Python e o ADBKit!
