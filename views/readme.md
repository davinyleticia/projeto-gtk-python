## Estrutura da Interface (`AppView`)
A classe `AppView` herda de `Gtk.Window` e constrói a seguinte estrutura de interface:

* **Janela Principal:** Configurada com bordas de 15px e tamanho padrão de 300x150 pixels.
* **Layout (`Gtk.Box`):** Utiliza uma caixa de orientação vertical com espaçamento de 10px para organizar os elementos um abaixo do outro.
* **Componentes Visuais:**
  * `instruction_label`: Um rótulo (`Gtk.Label`) instruindo o usuário a digitar algo.
  * `input_entry`: Um campo de texto (`Gtk.Entry`) para a entrada de dados do usuário.
  * `submit_button`: Um botão de envio (`Gtk.Button`) para processar a ação.
  * `result_label`: Um rótulo vazio (`Gtk.Label`) reservado para exibir o resultado retornado pelo sistema após o envio.
