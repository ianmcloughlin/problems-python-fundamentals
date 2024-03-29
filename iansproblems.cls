\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iansproblems}[2023/01/23 Ian's problems.]

\LoadClass[addpoints, 12pt, a4paper]{exam}

% Fonts.
\usepackage[T1]{fontenc}
% IBM Plex.
\usepackage[usefilenames,RMstyle={Text,Semibold},SSstyle={Text,Semibold},TTstyle={Text,Semibold},DefaultFeatures={Ligatures=Common}]{plex-otf}
% Math font.
\usepackage{plex-serif}
% Math as text.
\usepackage[basic,italic,symbolgreek]{mathastext}
% Set base font to sans serif.
\renewcommand*\familydefault{\sfdefault}

% More math layouts, equation arrays, etc.
\usepackage{amsmath}
% Enables the use of colour.
\usepackage{xcolor}
% Syntax high-lighting for code. Requires Python's pygments.
\usepackage{minted}
% Diagrams.
\usepackage{tikz}
% Allows for columns spanning multiple rows in tables.
\usepackage{multirow}
% Better looking tables, including nicer borders.
\usepackage{booktabs}
% More math symbols.
\usepackage{amssymb}
% More math fonts, like mathbb.
\usepackage{amsfonts}
% More theorem environments.
\usepackage{amsthm}
% More column formats for tables.
\usepackage{array}
% Adjust the sizes of box environments.
\usepackage{adjustbox}
% Better looking single quotes in verbatim and minted environments.
\usepackage{upquote}
% Better blank space decisions.
\usepackage{xspace}
% Better looking tikz trees.
\usepackage{forest}
% For plotting.
\usepackage{pgfplots}
% Tables.
\usepackage{tabularx}
% For more font sizes.
\usepackage{anyfontsize}
% Enables the use of umlauts and other accents.
\usepackage[utf8]{inputenc}
% Settings for captions, such as sideways captions.
\usepackage{caption}
% Symbols for units, like degrees and ohms.
\usepackage{gensymb}
% Calculates the number of pages.
\usepackage{lastpage}
% Bibliography.
\usepackage[style=verbose, autocite=footnote, backend=biber]{biblatex}
% Placeholder text.
\usepackage{lipsum}
% Line spacing.
\usepackage{setspace}

% Various tikz libraries.
% For drawing mind maps.
\usetikzlibrary{mindmap}
% For adding shadows.
\usetikzlibrary{shadows}
% Extra arrows tips.
\usetikzlibrary{arrows.meta}
% Old arrows.
\usetikzlibrary{arrows}
% Automata.
\usetikzlibrary{automata}
% For more positioning options.
\usetikzlibrary{positioning}
% Creating chains of nodes on a line.
\usetikzlibrary{chains}
% Fitting node to contain set of coordinates.
\usetikzlibrary{fit}
% Extra shapes for drawing.
\usetikzlibrary{shapes}
% For markings on paths.
\usetikzlibrary{decorations.markings}
% For advanced calculations.
\usetikzlibrary{calc}
% For layering.
\usetikzlibrary{backgrounds}

% PGF plots version.
\pgfplotsset{compat=1.18}

% ATU colours.
\definecolor{atunavy}{RGB}{0,26,121}
\definecolor{atuteal}{RGB}{123,185,203} 
\definecolor{atugreen}{RGB}{0,91,94}
\definecolor{atusand}{RGB}{255,232,212}
\definecolor{atuorange}{RGB}{255,121,30}
\definecolor{atuyellow}{RGB}{248,255,142}
\definecolor{atulightgreen}{RGB}{172,245,189}
\definecolor{atuwarmgrey}{RGB}{200,190,191}
\definecolor{atupurple}{RGB}{77,8,87}
\definecolor{atuoffwhite}{RGB}{237,237,237}

% Set minted up.
\usemintedstyle{igor}
\setminted{frame=single, framesep=2mm, bgcolor=atuoffwhite, baselinestretch=1.2}

% Prevent minted from showing errors.
\makeatletter
\expandafter\def\csname PYGdefault@tok@err\endcsname{\def\PYGdefault@bc##1{{\strut ##1}}}
\makeatother

% For displaying a blank character.
\newcommand{\bl}{\underline{\hspace{2mm}}}

% Question format.
\qformat{\textbf{Question \thequestion} \;\hfill \vrule depth 1em width 0pt}
\renewcommand{\partlabel}{\thepartno}
\renewcommand{\thepartno}{\textbf{(\alph{partno})}}
\pointformat{(\thepoints)}

% Drop points in right margin.
\pointsdroppedatright

% Use one and a half line spacing.
\onehalfspacing

\renewcommand{\partshook}{\setlength{\itemsep}{0.5cm}}

\addbibresource{bibliography.bib}