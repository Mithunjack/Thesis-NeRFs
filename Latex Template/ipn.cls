% A LaTeX template for Thesis submissions to Instituto Politécnico Nacional (IPN)
% José Luis Castro García (https://github.com/JoseLuisC99/IPN-thesis-template)
% Last Revision: September 2023

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipn}[2023/09/30 IPN thesis submission class]

\LoadClass[12pt, twoside]{book}
\RequirePackage[utf8]{inputenc}
\RequirePackage{xcolor}
\RequirePackage{geometry}
\RequirePackage[export]{adjustbox}
\RequirePackage{titlesec}

\definecolor{pantone_222_c}{RGB}{108, 29, 69}
\definecolor{black1}{RGB}{17, 17, 14}
\definecolor{gray1}{RGB}{54, 69, 79}
\geometry{
    a4paper,
    left=1in,
    right=1in,
    top=1in,
    bottom=1in
}




\def\schoolname#1{\def\@schoolname{#1}}
\def\degree#1{\def\@degree{#1}}
\def\advisor#1{\def\@advisor{#1}}
\def\coadvisor#1{\def\@coadvisor{#1}}
\def\academicyear#1{\def\@academicyear{#1}}
\coadvisor{}

\renewcommand{\maketitle}{
\begin{titlepage}
    \centering
    \begin{adjustbox}{max width=1.2\linewidth}
        \centering
        \begin{minipage}[c][0.99\textheight][t]{0.95\textwidth}
            \centering
            {\fontsize{22}{20}\selectfont\textbf{Christian-Albrechts-Universität zu Kiel\\}}
            \vspace{10pt}
            \begin{minipage}[t]{0.1\textwidth}
            \end{minipage}
            \hfill
            \begin{minipage}[t]{0.9\textwidth}
                {\color{pantone_222_c} \hrule width\textwidth height2.5pt}
            \end{minipage}
            \begin{minipage}[t]{0.9\textwidth}
                {\color{black1} \hrule width\textwidth height2.5pt}
            \end{minipage}
            \begin{minipage}[t]{0.1\textwidth}
            \end{minipage}
            
            \vspace{20pt}
            {\fontsize{16}{16}\selectfont\textsc{\@schoolname\\}}

                        
            \vspace{60pt}
            {\fontsize{25}{25}\selectfont\textbf{ Master Thesis}\\}
            \vspace{60pt}
            {\fontsize{16}{24}\selectfont\textbf{\@title\\}}

            \vspace{30pt}
            % {\fontsize{14}{14}\selectfont\textsc{Information systems and Data mining Group\\}}
            \vspace{10pt}


            \vspace{60pt}
            \vspace{10pt}
            {\fontsize{16}{16}\selectfont\textbf{\@author\\}}
            \vspace{10pt}
            {\fontsize{14}{14}\selectfont{\@degree\\}}

            \vspace{60pt}
            {\fontsize{14}{14}\selectfont\textsc{Supervisors\\}}
            \vspace{10pt}
            {\fontsize{14}{14}\selectfont\textbf{\@advisor}\\}
            \vspace{5pt}
            {\fontsize{14}{14}\selectfont\textbf{\@coadvisor}}

            \vfill
            {\fontsize{12}{12}\selectfont Kiel, Germany\\}
            \vspace{5pt}
            {\fontsize{12}{12}\selectfont 09.01.2024\\}
            \vspace{40pt}
        \end{minipage}
    \end{adjustbox}
\end{titlepage}
}

\titleformat{\chapter}[display]
{\bfseries\Large\centering}
{
    \filright
    \textsc{\textcolor{pantone_222_c}{
        \MakeUppercase{\chaptertitlename}
        \Huge
        \thechapter
    }}
}
{1ex}
{\Huge}
[\vspace{1ex}\titlerule]