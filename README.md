```text
projeto-gtl-python/
├── main.py
├── models/
│   ├── __init__.py
│   └── text_model.py
├── views/
│   ├── __init__.py
│   └── app_view.py
└── controllers/
    ├── __init__.py
    └── app_controller.py

```

Os arquivos `__init__.py` podem ficar vazios. Eles servem apenas para o Python reconhecer as pastas como módulos importáveis.

# Arquitetura do Projeto (MVC)

Este projeto foi estruturado utilizando o padrão de arquitetura **MVC (Model-View-Controller)**. Essa abordagem divide a aplicação em três componentes principais interconectados, separando a lógica de negócios da interface do usuário. Isso resulta em um código mais organizado, testável e fácil de manter.

Abaixo está a explicação de como o MVC foi aplicado neste projeto usando Python e GTK:

*   **Model (`models/`)**: É o cérebro dos dados. Responsável por gerenciar as informações, o estado e a lógica de negócios da aplicação. O *Model* é totalmente independente e não tem nenhum conhecimento sobre a interface gráfica (GTK).
*   **View (`views/`)**: Responsável exclusivamente pela interface com o usuário (UI). É aqui que construímos a janela, os botões, os campos de texto (`Gtk.Entry`) e os rótulos (`Gtk.Label`). A *View* apenas exibe os dados e capta as interações do usuário, sem processar a lógica por trás delas.
*   **Controller (`controllers/`)**: Atua como o maestro que orquestra a comunicação entre a *View* e o *Model*. Ele "escuta" os eventos gerados pela interface (como o clique de um botão), extrai os dados necessários, os envia para o *Model* processar/armazenar e, por fim, comanda a *View* para atualizar a tela com os resultados.

# Fluxo de Funcionamento

1. O usuário insere um texto e clica em "Enviar" na **View**.
2. A **View** dispara um sinal alertando o **Controller** sobre a ação.
3. O **Controller** lê o dado inserido na **View** e o envia para o **Model**.
4. O **Model** atualiza o seu estado interno com a nova informação.
5. O **Controller** recupera o dado validado/atualizado do **Model** e instrui a **View** a exibi-lo na tela.

   

# Configuração de Ambiente Virtual

```bash
python3 -m venv --system-site-packages venv

source venv/bin/activate

python --noconsole --onefile main.py

```

# if __name__ == "__main__":

```python

if __name__ == "__main__":
    model = TextModel()
    view = AppView()
    controller = AppController(model, view)

    view.show_all()
    Gtk.main()
```

Esse bloco é o coração da inicialização do seu aplicativo. Ele atua como o ponto de partida onde as três peças separadas da arquitetura MVC se encontram para dar vida ao programa.

* model = TextModel() e view = AppView(): O sistema cria as instâncias do Modelo (que guarda os dados) e da Visão (que desenha a tela). Neste ponto, eles ainda não sabem da existência um do outro.

* controller = AppController(model, view): Aqui ocorre a "Injeção de Dependência". Você passa o Modelo e a Visão para dentro do Controlador. É neste momento que o Controlador amarra tudo: ele pega os botões da Visão e conecta aos métodos dele, e sabe que deve atualizar aquele Modelo específico.

* view.show_all(): Pede ao GTK para pegar a janela principal (e todos os elementos dentro dela, como os campos de texto e botões) e finalmente renderizá-los na tela do usuário.

* Gtk.main(): Inicia o loop principal de eventos do GTK. É esse comando que mantém a janela aberta esperando o usuário clicar, digitar ou fechar o aplicativo. Sem ele, o script do Python simplesmente terminaria de rodar e a janela piscaria e fecharia instantaneamente.

# Dependência do sistema (Linux/Debian/Ubuntu)

O GTK 3 não é instalado via `pip`, ele é uma biblioteca do sistema operacional

```bash

sudo apt update
sudo apt install python3-gi python3-gi-cairo girl1.2-gtk-3.0 libgirepository1.0-dev

```
