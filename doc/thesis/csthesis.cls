%%
%%    File : csthesis.cls    (LaTeX2e class file)
%%  Author : Antal Buss, Mauricio Heredia
%% Version : 0.1
%% 
%% This file contains a class definition, csthesis, for the LaTeX2e
%% system which defines the layout of theses which are submitted in
%% the Department of Computer Science at the University of Edinburgh.
%%
%% For information on this class, please refer to "texdoc csthesis"
%%

\NeedsTeXFormat{LaTeX2e}[1994/12/01]
\ProvidesClass{csthesis}[1998/07/22 v0.1 Computer Science Thesis Class - PUJ]

%%
%% --- Initial Code ---
%%

\RequirePackage{ifthen}
\RequirePackage{vmargin}

\newcommand{\carrera}{INGENIERIA DE SISTEMAS Y COMPUTACION}
\newcommand{\titulo}{Mag\'{\i}ster en Ingenier\'{\i}a con \'Enfasis en Ingenier\'{\i}a de Sistemas y Computaci\'on.}
\newcommand{\carreramin}{Maestr\'{\i}a en Ingenier\'{\i}a de Sistemas y Computaci\'on}
\newcommand{\department}{FACULTAD DE INGENIERIA}
\newcommand{\university}{UNIVERSIDAD DEL VALLE}
\newcommand{\optar}{para optar el t\'{\i}tulo de}
\newcommand{\city}{SANTIAGO DE CALI}
\newcommand{\@chapteralignment}{\centering}
\newcommand{\draftmessage}{}
\newboolean{draftthesis}
\newboolean{usequotemarks}
\newboolean{usesinglespacing}
\newboolean{usedoublespacing}
\newboolean{usefullspacing}
\newboolean{usedeptreport}
\newboolean{useabbrevs}


%%
%%  --- Options ---
%%
%%  Current options: phd, mphil, msc, bsc, deptreport
%%                   draft
%%                   usequotes
%%                   singlespacing, doublespacing, fullspacing
%%                   centerchapter, leftchapter, rightchapter,
%%                   + all report.cls options
%%

% Modify by Mauricio Heredia R.
\DeclareOption{bsc}{\newcommand{\doctype}{Tesis de grado}}
\DeclareOption{ante}{\newcommand{\doctype}{Anteproyecto de grado}}

\newcommand{\degreetext} {\university\\ \department\\ \carrera}
\newcommand{\letrero} {\doctype~\optar\\ \titulo}
\newcommand{\letdirector} {Director}

\DeclareOption{centerchapter,centrechapter}
   {\renewcommand{\@chapteralignment}{\centering}}
\DeclareOption{leftchapter}
   {\renewcommand{\@chapteralignment}{\raggedright}}
\DeclareOption{rightchapter}
   {\renewcommand{\@chapteralignment}{\raggedleft}}

\DeclareOption{draft}{
   \setboolean{draftthesis}{true}
   \renewcommand{\draftmessage}{(Draft Copy)}}
\DeclareOption{usequotes}{\setboolean{usequotemarks}{true}}

\DeclareOption{abbrevs}{\setboolean{useabbrevs}{true}}

\DeclareOption{singlespacing}{\setboolean{usesinglespacing}{true}}
\DeclareOption{doublespacing}{\setboolean{usedoublespacing}{true}}
\DeclareOption{fullspacing}{\setboolean{usefullspacing}{true}}

\DeclareOption{deptreport}{\setboolean{usedeptreport}{true}}

\DeclareOption{parskip}{\AtEndOfClass{\input{parskip.clo}}}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}

\ExecuteOptions{phd,centerchapter} % the default options
\ProcessOptions

%%
%% --- Class Loading (built ontop of report.cls) ---
%%

\LoadClass[letterpaper,12pt]{report}

%%
%% --- Main Code ---
%%

\newboolean{isspecialchapter}
\setboolean{isspecialchapter}{false}

%%
%% First we will sort out the page layout. The following is a brief
%% summary of the university typesetting regulations:
%%   Printed on A4 paper, entirely on rectos (single-sided)
%%   4cm binding margin
%%   2cm head margin
%%   2.5cm fore-edge margin
%%   4cm tail margin
%%   spacing: not less then 1.5 spacing (18pt leading)
%%            quotations & footnotes in single spacing
%%            bibliography may be in single spacing
%%   character size: not exceed 12pt for body text (at least 10pt)
%%   style: a serif font should be used
%%  hyphenation should be avoided if possible
%%

%% First we will set out the margins as defined above. We use the vmargin
%% package to simplify this process. However, every printer in the
%% department outputs pages of subtly different size and position. We
%% therefore provide support for a number of printers, as they are
%% currently configured.
%%
%%  \setmarginsrb{leftmargin}{topmargin}{rightmargin}{bottommargin}%
%%               {headheight}{headsep}{footheight}{footskip}

%\setpapersize{A4}

% T.B. addition \/
\setpapersize{USletter}


\newcommand{\SetPrinterEpson}{%
   \setmarginsrb{3.0cm}{1.0cm}{3.0cm}{3.0cm}% 
                {14pt}{20pt}{11pt}{22pt}%
}
% ------------- /\
\newcommand{\SetPrinterLWfourteen}{%
   \setmarginsrb{3.8cm}{0.65cm}{2.7cm}{3.3cm}% 
                {14pt}{20pt}{12pt}{22pt}%
}
\newcommand{\SetPrinterHPtwentyfour}{%
   \setmarginsrb{3.9cm}{1.05cm}{2.6cm}{3.0cm}% 
                {14pt}{20pt}{12pt}{22pt}%
}
\newcommand{\SetPrinterHPsixteen}{%
   \setmarginsrb{4.05cm}{0.9cm}{2.45cm}{3.2cm}% 
                {14pt}{20pt}{12pt}{22pt}%
}
\newcommand{\SetPrinterMPsixteen}{%
   \setmarginsrb{4.0cm}{0.8cm}{2.45cm}{3.25cm}% 
                {14pt}{20pt}{12pt}{22pt}%
}
\newcommand{\SetPrinterDraft}{%
   \setmarginsrb{1in}{0.4in}{1in}{1in}% 
                {14pt}{20pt}{12pt}{22pt}%
}


\newcommand{\PrtMsg}[1]{\typeout{NOTE: Setting page margins for printer #1.}}
\newcommand{\SetPrinter}[1]{%
   \ifthenelse{\equal{#1}{lw14}}{\SetPrinterLWfourteen\PrtMsg{#1}}{%
   \ifthenelse{\equal{#1}{hp24}}{\SetPrinterHPtwentyfour\PrtMsg{#1}}{%
   \ifthenelse{\equal{#1}{hp16}}{\SetPrinterHPsixteen\PrtMsg{#1}}{%
   \ifthenelse{\equal{#1}{mp16}}{\SetPrinterMPsixteen\PrtMsg{#1}}{%
      \typeout{WARNING: Invalid printer choice: #1. Defaulting to hp24.}
      \SetPrinterHPtwentyfour
   }}}}
}

%\SetPrinterHPtwentyfour
\SetPrinterEpson

%%
%% Hack to make minitoc work with csthesis. We declare a new chapter
%% variable called starchapter to be used by \addcontentsline when we
%% add contents lines for List of Figures/Tables. If we don't, then
%% minitoc treats the LOF/LOT sections as chapters of the thesis.
%%

\@ifundefined{chapter}{}{\let\l@starchapter\l@chapter}

%%
%% This bit will set up the header format for the thesis.
%% This currently uses a "headings" style showing the pagenumber
%% and chapter number/title. (in slanted text)
%%

\renewcommand{\chaptermark}[1]{\markboth{#1}{#1}}
\newcommand{\chapternoheader}{
  \ifthenelse{\boolean{isspecialchapter}}
    {}
    {\chaptername\ \thechapter\ \ ---\ }
}

\newcommand{\headfootstyle}{\normalsize}  % font size of headers and footers

\renewcommand{\ps@headings}{
  \renewcommand{\@oddfoot}{}
  \renewcommand{\@evenfoot}{}
  \renewcommand{\@evenhead}{\headfootstyle\thepage\hfil\sl\chapternoheader%
                            \leftmark\ \draftmessage}
  \renewcommand{\@oddhead}{\hskip -0.35em {\sl\headfootstyle\chapternoheader%
                           \rightmark\ \draftmessage}\hfil\thepage}
}

\renewcommand{\ps@plain}{
  \renewcommand{\@oddfoot}{\hfil\headfootstyle\thepage\hfil}
  \renewcommand{\@evenfoot}{\hfil\headfootstyle\thepage\hfil}
  \renewcommand{\@evenhead}{}
  \renewcommand{\@oddhead}{}
}

%%
%% And now setup that headings style as default
%%

\newcommand{\@textpagenumbering}{arabic}
\newcommand{\@preamblepagenumbering}{roman}
\newcommand{\@textpagestyle}{plain}
\newcommand{\@preamblepagestyle}{plain}

\pagestyle{\@preamblepagestyle}

\setcounter{secnumdepth}{6}

%%
%% Set up the default names for the various chapter headings
%%

\renewcommand{\contentsname}{Indice General}
\renewcommand{\listfigurename}{Indice de Figuras}
\renewcommand{\listtablename}{Indice de Tablas}
\newcommand{\listanexoname}{\'Indice de Anexos}
\renewcommand{\bibname}{Bibliograf'ia}
\renewcommand{\indexname}{Indicie}
\renewcommand{\abstractname}{Resumen}

%%
%% Some sundry commands which are generally useful...
%%

\ifthenelse{\boolean{useabbrevs}}
 {\RequirePackage{xspace}
  \newcommand{\NB}{N.B.\@\xspace}
  \newcommand{\eg}{e.g.\@\xspace}
  \newcommand{\Eg}{E.g.\@\xspace}
  \newcommand{\ie}{i.e.\@\xspace}
  \newcommand{\Ie}{I.e.\@\xspace}
  \newcommand{\etc}{etc.\@\xspace}
  \newcommand{\etal}{{\em et al}.\@\xspace}
  \newcommand{\etseq}{{\em et seq}.\@\xspace}
  \newcommand{\precis}{pr\'ecis\xspace}
  \newcommand{\Precis}{Pr\'ecis\xspace}
  \newcommand{\role}{r\^ole\xspace}
  \newcommand{\Role}{R\^ole\xspace}
  \newcommand{\naive}{na\"\i ve\xspace}
  \newcommand{\Naive}{Na\"\i ve\xspace}
  \newcommand{\tm}{\raisebox{1ex}{\tiny TM}\xspace}
  \newcommand{\cpright}{\raisebox{1ex}{\tiny\copyright}\xspace}
  \newcommand{\degrees}{\raisebox{1.2ex}{\tiny\ensuremath{\circ}}\xspace}}
 {}

%%
%% Set up the double spacing and provide commands to alter the
%% spacing for the subsequent text. By default, 1.5 spacing will be
%% used. This can be modified through the singlespacing, doublespacing
%% or draft class options.
%%

\ifthenelse{\boolean{usefullspacing}}
   {\newcommand{\doublespace}{\setlength{\baselineskip}{28.8pt}}
    \newcommand{\oneandahalfspace}{\setlength{\baselineskip}{21.6pt}}}
   {\newcommand{\doublespace}{\setlength{\baselineskip}{24pt}}
    \newcommand{\oneandahalfspace}{\setlength{\baselineskip}{18pt}}}
\newcommand{\singlespace}{\setlength{\baselineskip}{14.4pt}}

\ifthenelse{\boolean{draftthesis}}
   {\AtBeginDocument{\singlespace}\SetPrinterDraft}{
   \ifthenelse{\boolean{usesinglespacing}}
      {\AtBeginDocument{\singlespace}}{
      \ifthenelse{\boolean{usedoublespacing}}
         {\AtBeginDocument{\doublespace}}
         {\AtBeginDocument{\oneandahalfspace}}
   }
}

%%
%% When printing twosided, then the title page must be followed by
%% a blank page so that the thesis begins on the right-hand page. 
%% Also we must ensure that the thesis ends on a lef-hand page. We
%% do the latter by issuing a \cleardoublepage at the end of document.
%%

\newcommand{\cscleardoublepage}%
  {\vfill\pagebreak\thispagestyle{empty}\cleardoublepage}
\AtEndDocument{\cscleardoublepage}

%%
%% A couple of commands for figures/captions
%%

\newcommand{\thesiscaption}[3][]{
   \ifthenelse{\equal{#1}{}}
     {\parbox{5in}{\caption{{\em #2\/}}\label{#3}}}
     {\parbox{5in}{\caption[#1]{{\em #2\/}}\label{#3}}}
}

%%
%% Quotations are supposed to be in single-space, so we will
%% explicitly redefine the quotation env. to support this.
%% And introduce a citetext env. which can add an attribution.
%%

\renewenvironment{quotation}
   {\begin{quote}\singlespace
    \ifthenelse{\boolean{usequotemarks}}{``}{}\sl}
   {\ifthenelse{\boolean{usequotemarks}}{\rm''}{}\end{quote}}

\newcommand{\citationname}{}
\newenvironment{citetext}[1]
   {\renewcommand{\citationname}{#1}\begin{quote}\singlespace
    \ifthenelse{\boolean{usequotemarks}}{``}{}\sl}
   {\ifthenelse{\boolean{usequotemarks}}{\rm''}{}
    \hspace*{\fill}\nolinebreak[1]\hspace*{\fill}
    \rm (\citationname)\end{quote}}

%%
%% Let's have a dedication page so I can thank my mummy.
%%

\newcommand{\dedication}[1]
   {\titlepage\null\vspace{2.5in}
   \begin{flushleft}\raggedleft #1\end{flushleft}
%    \begin{center}#1\end{center}
    \par\vfil\null\endtitlepage\cscleardoublepage}


%%
%% Para las paginas con los anexos
%% 

\newenvironment{anexo}[2]
   {\cscleardoublepage
    \ifthenelse{\equal {#1}{1}}{\addcontentsline{toc}{chapter}{ANEXOS}}{}
%ojo aqui
    \addcontentsline{loa}{section}{#2}
    \null\vspace{2.5in}
    \par\vfil\null
    \begin{center}{\bf #2}\end{center}
    \par\cscleardoublepage
    {\Large #2} \vspace{0.7cm} \newline
    }
    {\par\vfil\null} 



%%
%% Now let's redefine the abstract env. so that the title is 
%% comparable to other chapter headings. Also have abstract
%% start at top of page instead of floating in the middle
%%

\renewenvironment{abstract}
   {\cscleardoublepage\null\vspace{1cm}
    \begin{center}
       \bfseries \LARGE\abstractname
    \end{center}}
   {\par\vfil\null\cscleardoublepage}


%\renewenvironment{abstract}
%   {\titlepage\null\vspace{1cm}
%    \begin{center}
%       \bfseries \LARGE\abstractname
%    \end{center}}
%   {\par\vfil\null\endtitlepage}

%%
%% Based upon the above abstract env., provide wrappers for
%% an acknowledgements and declation env.
%%

\newenvironment{acknowledgements}
   {\renewcommand{\abstractname}{Agradecimientos}\begin{abstract}}
   {\end{abstract}\renewcommand{\abstractname}{Abstract}}   

\newenvironment{declaration}
   {\renewcommand{\abstractname}{Declaraci\'on}\begin{abstract}}
   {\end{abstract}\renewcommand{\abstractname}{Abstract}}   


\newcommand{\nullpage}[1]
   {\titlepage\null\vspace{2.5in}
 \begin{flushleft}#1\end{flushleft}
    \par\vfil\null\endtitlepage\cscleardoublepage}%\raggedright}



\newcommand{\art}
{  \titlepage\null\vspace{2.5in}
   \begin{flushleft}
   \raggedleft
   ARTICULO 23 de la Resoluci\'on No 13 del 6 de Julio de 1946\\
   del Reglamento de la Pontificia Universidad Javeriana.\\
   \vspace{0.2in}
   ``La Universidad no se hace responsable por los conceptos emitidos\\
   por sus alumnos en sus trabajos de Tesis. S\'olo velar\'a porque no se \\
   publique nada contrario al dogma y a la moral Cat\'olica y porque las\\
   Tesis no contengan ataques o pol\'emicas puramente personales;\\
   antes bien, se vea en ellas el anhelo de buscar la Verdad y la Justicia''\\
   \end{flushleft}\par\vfil\null\endtitlepage\cscleardoublepage
}


\newcommand{\cartadir}
{
  \titlepage\null\vspace{2cm}
  Santiago de Cali, \@fechacartas\\
  \vspace{1.3cm}
  \newline
  Doctor\\
  \@decano \\
  Decano Acad\'emico de la Facultad de Ingenier\'{\i}a\\
  Universidad del Valle\\
  Ciudad\\
  \vspace{1.3cm}
  \newline
  Certifico que el presente proyecto de grado, titulado ``\@title'' realizado por \@fauthor, estudiante de \carreramin, se encuentra terminado y puede ser presentado para sustentaci\'on.
  \vspace{2cm}
  \newline
  Atentamente,\\
  \vspace{3cm}
  \newline 
  Ing. \@director\\
  Director del Proyecto
\par\vfil\endtitlepage\cscleardoublepage
}



\newcommand{\cartaauthor}
{
  \titlepage\null\vspace{2cm}
  Santiago de Cali, \@fechacartas\\
  \vspace{1.3cm}
  \newline
  Doctor\\
  \@decano \\
  Decano Acad\'emico de la Facultad de Ingenier\'{\i}a\\
  Universidad del Valle\\
  Ciudad\\
  \vspace{1.3cm}
  \newline
  Por medio de \'esta, presentamos a usted el proyecto de grado titulado ``\@title'' para optar el t\'{\i}tulo de \titulo.
  \vspace{0.8cm} \\
  Esperamos que este proyecto re\'una todos los requisitos acad\'emicos y cumpla el prop\'osito para el cual fue creado, y sirva de apoyo para futuros proyectos en la Universidad Javeriana relacionados con la materia.
  \vspace{1.3cm}
  \newline
  Atentamente,
  \vspace{1.5cm}
  \newline 
  \begin{center}
  \begin{tabular}{rcl}
  \@fauthor & ~~~~~~ & \@sauthor \\
  \end{tabular}
  \end{center}
  \par\vfil\endtitlepage\cscleardoublepage
}


\newcommand{\acepta}
{
  \titlepage\null\vspace{1cm}
  \begin{flushleft}
  \raggedleft
  Nota de Aceptaci\'on:\\
  \vspace{0.8cm}
  Aprobado por el comit\'e de Trabajo de Grado en\\
  cumplimiento de los requisitos exigidos por la\\
  Universidad del valle para optar el\\
  t\'{\i}tulo de \titulo.\\
  \end{flushleft}
  \vspace{2.5cm}
  \begin{center}
  \@decano \\
  Decano Acad\'emico de la Facultad de Ingenier\'{\i}a\\
  \end{center}
  \vspace{2.5cm}
  \begin{center}
  \begin{tabular}{ccc}
  \@directorcar & ~~~~~~ & \@director\\
  Director de la Carrera de Ingenier\'{\i}a & & Director de Tesis\\
  de Sistemas y Computaci\'on\\ 
  \vspace{2.5cm} \\
  \@fjurado & ~~~~~~ & \@sjurado\\
  Jurado & & Jurado\\
  \end{tabular}
  \end{center}
  \par\vfil\endtitlepage\cscleardoublepage
}




%%
%% Now let's look at the format for the title page of the
%% thesis. This is done by redefining \maketitle, and allowing
%% some extra input options: \submityear and \graduationdate
%%

\def\submityear#1{\gdef\@submityear{#1}}
\gdef\@submityear{\the\year}

% added by Mauricio Heredia R. feb 20/1998
\def\fauthor#1{\gdef\@fauthor{#1}}
\gdef\@fauthor{}
\def\sauthor#1{\gdef\@sauthor{#1}}
\gdef\@sauthor{}
\def\director#1{\gdef\@director{#1}}
\gdef\@director{}
\def\directorcar#1{\gdef\@directorcar{#1}}
\gdef\@directorcar{}
\def\directortitle#1{\gdef\@directortitle{#1}}
\gdef\@directortitle{}
\def\decano#1{\gdef\@decano{#1}}
\gdef\@decano{}
\def\fjurado#1{\gdef\@fjurado{#1}}
\gdef\@fjurado{}
\def\sjurado#1{\gdef\@sjurado{#1}}
\gdef\@sjurado{}
\def\fechacartas#1{\gdef\@fechacartas{#1}}
\gdef\@fechacartas{}

\def\graduationdate#1{\gdef\@graduationdate{#1}}
\gdef\@graduationdate{}

\ifthenelse{\boolean{usedeptreport}}{
   \renewcommand{\maketitle}{
      \begin{titlepage}
      \addtolength{\oddsidemargin}{-0.75cm}
      \begin{center}
      \null\vskip 6.1cm
      \begin{minipage}[t][7.6cm]{10.5cm}
         \begin{center}
         {\LARGE\bfseries \@title \par
            \ifthenelse{\boolean{draftthesis}}{\large \draftmessage}{}
         }\vfil
         {\slshape \@fauthor \\ \@sauthor \par}
         \end{center}
      \end{minipage}
      \vfil
      {\degreetext \\ \@submityear  \par}
      \ifthenelse{\equal{\@graduationdate}{}}{}
         {\vskip 1cm {\large \ttfamily (Graduation date:\@graduationdate)}}
      \end{center}
      \end{titlepage}\cscleardoublepage
   }}{
   \renewcommand{\maketitle}{
      \begin{titlepage}\begin{center}
      \null\vfil\vskip 60\p@
      {\LARGE\bfseries \@title \par
         \ifthenelse{\boolean{draftthesis}}{\large (Draft Copy)}{}
      }\vfill
      {\slshape \@fauthor \\ \@sauthor \par}\vskip 1cm\vfill
      {\degreetext \\ \city \\ \@submityear \par}
      \vskip 1cm 
      \ifthenelse{\equal{\@graduationdate}{}}{}
         {{\large \ttfamily (Graduation date:\@graduationdate)}}
      \end{center}\end{titlepage}\cscleardoublepage
   }}


%**************************
% added by Mauricio Heredia R. feb 20 1998

\ifthenelse{\boolean{usedeptreport}}{
   \newcommand{\makecontitle}{
      \begin{titlepage}
      \addtolength{\oddsidemargin}{-0.75cm}
      \begin{center}
      \null\vskip 6.1cm
      \begin{minipage}[t][7.6cm]{10.5cm}
         \begin{center}
         {\LARGE\bfseries \@title \par
            \ifthenelse{\boolean{draftthesis}}{\large \draftmessage}{}
         }\vfil
         {\slshape \@fauthor \\\@sauthor \par}
         {\slshape \letrero \par}
         {\slshape \letdirector \\ \@director \\ \@directortitle \par}
         \end{center}
      \end{minipage}
      \vfil
      {\degreetext \\ \@submityear \par}
      \ifthenelse{\equal{\@graduationdate}{}}{}
         {\vskip 1cm {\large \ttfamily (Graduation date:\@graduationdate)}}
      \end{center}
      \end{titlepage}\cscleardoublepage
   }}{
   \newcommand{\makecontitle}{
      \begin{titlepage}\begin{center}
      \null\vfil\vskip 60\p@
      {\LARGE\bfseries \@title \par
         \ifthenelse{\boolean{draftthesis}}{\large (Draft Copy)}{}
      }\vfill
      {\slshape \@fauthor \\ \@sauthor \par}\vskip 1cm\vfill
      {\slshape \letrero  \par}\vskip 1cm\vfill
      {\slshape \letdirector \\ \@director \\ \@directortitle \par}\vskip 1cm\vfill
      {\degreetext \\ \city \\ \@submityear \par}
      \vskip 1cm 
      \ifthenelse{\equal{\@graduationdate}{}}{}
         {{\large \ttfamily (Graduation date:\@graduationdate)}}
      \end{center}\end{titlepage}\cscleardoublepage
   }}


%**************************


%%
%% Now we can redefine the chapter headings, with the flexibility
%% to choose whether we want the headings to be left, right or
%% centre justified. N.B. Most of this code is replicated from
%% the utthesis.sty style: version 1.0, (c) 1994 Dinesh Das
%%

\newcommand{\specialchapter}[1]{
   \chapter*{#1\@mkboth{\MakeUppercase#1}{\MakeUppercase#1}}
   \addcontentsline{toc}{chapter}{#1}
   \chaptermark{#1}
   \setboolean{isspecialchapter}{true}
}

\renewcommand{\chapter}{\clearpage
   \thispagestyle{plain}%
%   \setboolean{isspecialchapter}{false}
   \global\@topnum\z@
   \@afterindentfalse
   \secdef\@chapter\@schapter
   }

%%%
%%% Command from report.cls, (c) LaTeX3 Project.
%%%


\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
%                     Aumenta el numero
                      \refstepcounter{chapter}%
                      \typeout{\@chapapp\space\thechapter.}%
                      \addcontentsline{toc}{chapter}%
                             {\protect\numberline{\thechapter}#1}%
% deleted by mhr 
%                             {\@chapapp\ \protect\numberline{\thechapter}#1}%
                    \else
                      \addcontentsline{toc}{chapter}{\@chapapp\ #1}
                    \fi
                    \ifnum\value{chapter}=1\pagestyle{\@textpagestyle}\fi%
                    \chaptermark{#1}%
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \addtocontents{loa}{\protect\addvspace{10\p@}}%
                    \@makechapterhead{#2}%
                    \@afterheading
                    }
%%%
%%% Command from report.cls, (c) LaTeX3 Project.
%%%

\def\@makechapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \@chapteralignment \reset@font
    \ifnum \c@secnumdepth >\m@ne
%% modify by mhr
%      \huge\bfseries \@chapapp{} \thechapter
      \huge\bfseries \thechapter
% deleted by mhr
%      \par
%      \vskip 20\p@
    \fi
    \Huge ~ \bfseries #1\par
    \nobreak
    \vskip 40\p@
  }}
\def\@makeschapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \@chapteralignment
    \reset@font
    \Huge \bfseries  #1\par
    \nobreak
    \vskip 40\p@
  }}

%\newcommand{\setbibliographyheader}{
%   \chaptermark{\bibname}
%   \setboolean{isspecialchapter}{true}
%}

%%
%% Updated thebibliography environment. 
%% Modified from report.cls v1.3q (c) LaTeX3 Project.
%% Now includes entry in contents page & supports title rejustifying
%%

\renewenvironment{thebibliography}[1]
     {\specialchapter{\bibname}
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy\clubpenalty4000\widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}


\newenvironment{posiblebibliografia}[1]
     {\list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}}%
%      \sloppy\clubpenalty4000\widowpenalty4000%
%      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}


%%
%% Updated listoftables environment. 
%% Modified from report.cls v1.3q (c) LaTeX3 Project.
%% Now includes entry in contents page & supports title rejustifying
%%

\renewcommand\listoftables{%
    \chapter*{\listtablename
      \@mkboth{%
          \MakeUppercase\listtablename}{\MakeUppercase\listtablename}}%
     \addcontentsline{toc}{starchapter}{\listtablename} 
    \@starttoc{lot}%
    }

%%
%% Updated listoffigures environment. 
%% Modified from report.cls v1.3q (c) LaTeX3 Project.
%% Now includes entry in contents page & supports title rejustifying
%%

\renewcommand\listoffigures{%
    \chapter*{\listfigurename
      \@mkboth{\MakeUppercase\listfigurename}%
              {\MakeUppercase\listfigurename}}%
    \addcontentsline{toc}{starchapter}{\listfigurename}
    \@starttoc{lof}%
    }


%%
%% listofanexos environment. 
%% Created by mhr.
%% Now includes entry in contents page & supports title rejustifying
%%

\newcommand\listofanexos{%
    \chapter*{\listanexoname
      \@mkboth{%
          \MakeUppercase\listanexoname}{\MakeUppercase\listanexoname}}%
     \addcontentsline{toc}{starchapter}{\listanexoname} 
    \@starttoc{loa}%
    }


%%
%% Redefine the appendix command to ensure that it does a pagebreak
%% (sorts problem of Appendix appearing in header of last page before
%% the first apppendix).
%%

\renewcommand{\appendix}{\vfill\pagebreak
  \setcounter{chapter}{0}%
  \setcounter{section}{0}%
  \renewcommand\@chapapp{\appendixname}%
  \renewcommand\chaptername{\appendixname}%
  \renewcommand\thechapter{\@Alph\c@chapter}
}

%%
%% EOF: csthesis.cls
%%




