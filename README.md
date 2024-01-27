# leitor_de_escalas_musicais.py
<h1 align="center"> Sobre </h1>
<p></p><a href="https://github.com/raphaelfaber/leitor_de_escalas_musicais.py/tree/main"> leitor_de_escalas_musicais</a> é um projeto simples de linha de comando que busca facilitar o estudo de musicistas iniciantes.
Ao digitar alguma nota, ele monta:</p>
<ul>
 <li>Escala Maior</li>
 <li>Escala Menor</li>
 <li>Campo Harmônico</li>
</ul>

<h1 align="center"> Como usar </h1>
<h2>1) Instalar o Python3</h1>
<p>Caso você não tenha o python3 instalado no seu sistema, basta executar o comando abaixo:</p>
<ul>
 <li>
   <p>Debian e derivados:</p>
   <code>command -v python3 &> /dev/null && echo python3 já instalado || echo instalando python... && sudo apt-get install -y python3</code>
 </li>
  <li>
   <p>Red Hat e derivados:</p>
   <code>command -v python3 &> /dev/null && echo python3 já instalado || echo instalando python... && sudo yum install -y python3</code>
 </li>
</ul>
<h2>2) Fazer o download dos fonts</h2>
<p>Basta clonar o repositório ou fazer download do arquivo .zip e extrair na pasta de preferência. para clonar o repositório para a sua pasta home:</p>
<code>   git clone https://github.com/raphaelfaber/leitor_de_escalas_musicais.py $HOME/leitor_de_escalas_musicais</code>

<h2>3) Executar o programa</h2>
<p>Uma vez que os fonts estiverem no seu dispositivo,Basta executar o arquivo leitor_de_escalas_musicais.py no diretório raiz do projeto. Se Você fez o download usando o comando acima, basta executar:</p>
<code> python3 $HOME/leitor_escalas_musicais/programa_principal.py</code>
<p>Ao executar o programa, será exibido o menu principal:</p>
<img src="https://github.com/raphaelfaber/leitor_de_escalas_musicais.py/assets/90429070/be6a970d-e0d6-4e52-ba7e-1d53a377aa64">
<p>Selecione a nota desejada e o programa irá imprimir a escala maior, menor e campo harmônico da nota selecionada.</p>
<p><b>Atenção: O programa suporta as notas normais e sustenidas (#), o programa NÃO suporta notas bemol (b).</b></p>

<h1> Quer contribuir? </h1>
<p> Esse projeto tem o propósito de ajudar. Apenas isso e nada mais que isso. Portanto, para que o programa cumpra o seu propósito, ele deve ser acessível para quem precisar. Mesmo que essa pessoa seja completamente leiga. Então, para contribuir você pode:</p>
<ul>
 <li>Divulgar para os potenciais interessados</li>
 <li>Reportar bugs e problemas</li>
 <li>Traduzir para outros idiomas</li>
 <li>Acompanhar e auxiliar com os issues</li>
</ul>
<p>No entanto, se quisermos levar o projeto a um outro nível, podemos:</p>
<ul>
 <li>Criar uma interface gráfica amigável</li>
 <li>Desenvolver esse programa em web, tornando-o mais acessível</li>
 <li>Desenvolver uma versão mobile</li>
</ul>
