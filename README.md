% Options for packages loaded elsewhere
\PassOptionsToPackage{unicode}{hyperref}
\PassOptionsToPackage{hyphens}{url}
%
\documentclass[
]{article}
\usepackage{amsmath,amssymb}
\usepackage{iftex}
\ifPDFTeX
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \usepackage{textcomp} % provide euro and other symbols
\else % if luatex or xetex
  \usepackage{unicode-math} % this also loads fontspec
  \defaultfontfeatures{Scale=MatchLowercase}
  \defaultfontfeatures[\rmfamily]{Ligatures=TeX,Scale=1}
\fi
\usepackage{lmodern}
\ifPDFTeX\else
  % xetex/luatex font selection
\fi
% Use upquote if available, for straight quotes in verbatim environments
\IfFileExists{upquote.sty}{\usepackage{upquote}}{}
\IfFileExists{microtype.sty}{% use microtype if available
  \usepackage[]{microtype}
  \UseMicrotypeSet[protrusion]{basicmath} % disable protrusion for tt fonts
}{}
\makeatletter
\@ifundefined{KOMAClassName}{% if non-KOMA class
  \IfFileExists{parskip.sty}{%
    \usepackage{parskip}
  }{% else
    \setlength{\parindent}{0pt}
    \setlength{\parskip}{6pt plus 2pt minus 1pt}}
}{% if KOMA class
  \KOMAoptions{parskip=half}}
\makeatother
\usepackage{xcolor}
\ifLuaTeX
  \usepackage{luacolor}
  \usepackage[soul]{lua-ul}
\else
  \usepackage{soul}
\fi
\setlength{\emergencystretch}{3em} % prevent overfull lines
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-\maxdimen} % remove section numbering
\ifLuaTeX
  \usepackage{selnolig}  % disable illegal ligatures
\fi
\IfFileExists{bookmark.sty}{\usepackage{bookmark}}{\usepackage{hyperref}}
\IfFileExists{xurl.sty}{\usepackage{xurl}}{} % add URL line breaks if available
\urlstyle{same}
\hypersetup{
  hidelinks,
  pdfcreator={LaTeX via pandoc}}

\author{}
\date{}

\begin{document}

\textbf{Picom}

\emph{\textbf{\ul{Mode d'emploi d'utilisation}}}

\emph{\textbf{\ul{\hfill\break
}}}

\section{Table des matières}\label{table-des-matiuxe8res}

\hyperref[bibliothuxe8que]{Bibliothèque \hyperref[bibliothuxe8que]{3}}

\hyperref[liste-des-bibliothuxe8ques-utilisuxe9es]{1. Liste des
bibliothèques utilisées :
\hyperref[liste-des-bibliothuxe8ques-utilisuxe9es]{3}}

\hyperref[comment-installer-les-bibliothuxe8ques-nuxe9cessaires]{2.
Comment installer les bibliothèques nécessaires :
\hyperref[comment-installer-les-bibliothuxe8ques-nuxe9cessaires]{3}}

\hyperref[duxe9tails-des-bibliothuxe8ques-installuxe9es]{2.1 Détails des
bibliothèques installées :
\hyperref[duxe9tails-des-bibliothuxe8ques-installuxe9es]{4}}

\hyperref[descriptif-du-code]{Descriptif du code
\hyperref[descriptif-du-code]{4}}

\hyperref[importation-des-bibliothuxe8ques]{1. Importation des
Bibliothèques \hyperref[importation-des-bibliothuxe8ques]{4}}

\hyperref[configuration-des-paramuxe8tres]{2. Configuration des
Paramètres \hyperref[configuration-des-paramuxe8tres]{5}}

\hyperref[fonctions-principales]{3. Fonctions Principales
\hyperref[fonctions-principales]{5}}

\hyperref[a.-capture-et-diffusion-viduxe9o]{a. Capture et Diffusion
Vidéo \hyperref[a.-capture-et-diffusion-viduxe9o]{5}}

\hyperref[b.-capture-et-diffusion-audio]{b. Capture et Diffusion Audio
\hyperref[b.-capture-et-diffusion-audio]{5}}

\hyperref[c.-gestion-des-commandes]{c. Gestion des Commandes
\hyperref[c.-gestion-des-commandes]{5}}

\hyperref[d.-interface-utilisateur-tkinter]{d. Interface Utilisateur
(Tkinter) \hyperref[d.-interface-utilisateur-tkinter]{5}}

\hyperref[gestion-des-threads]{4. Gestion des Threads
\hyperref[gestion-des-threads]{6}}

\hyperref[boucle-principale-de-linterface]{5. Boucle Principale de
l\textquotesingle Interface
\hyperref[boucle-principale-de-linterface]{6}}

\hyperref[explication-de-la-connexion-entre-les-deux-raspberry-pi]{Explication
de la Connexion entre les Deux Raspberry Pi
\hyperref[explication-de-la-connexion-entre-les-deux-raspberry-pi]{7}}

\hyperref[configuration-du-ruxe9seau-wi-fi-local]{1. Configuration du
Réseau Wi-Fi Local \hyperref[configuration-du-ruxe9seau-wi-fi-local]{7}}

\hyperref[configuration-du-ruxe9seau-ethernet]{2. Configuration du
Réseau Ethernet \hyperref[configuration-du-ruxe9seau-ethernet]{7}}

\hyperref[communication-entre-les-deux-raspberry-pi]{3. Communication
entre les Deux Raspberry Pi
\hyperref[communication-entre-les-deux-raspberry-pi]{8}}

\hyperref[fonctionnement-de-linterface-administrateur]{4. Fonctionnement
de l\textquotesingle Interface Administrateur
\hyperref[fonctionnement-de-linterface-administrateur]{8}}

\hyperref[installation-os-et-emplacement-du-code]{Installation OS et
Emplacement du code
\hyperref[installation-os-et-emplacement-du-code]{9}}

\hyperref[astuce]{Astuce \hyperref[astuce]{9}}

\section{}\label{section}

\section{\texorpdfstring{\hfill\break
}{ }}\label{section-1}

\section{Bibliothèque}\label{bibliothuxe8que}

\subsection{1. Liste des bibliothèques utilisées
:}\label{liste-des-bibliothuxe8ques-utilisuxe9es}

\begin{quote}
\textbf{Bibliothèques standards de Python (installées par défaut avec
Python3) :}
\end{quote}

\begin{itemize}
\item
  \textbf{socket} : Permet la communication réseau entre les Raspberry
  Pi via des sockets.
\item
  \textbf{struct} : Permet de manipuler des données en C, utile pour les
  communications binaires.
\item
  \textbf{threading} : Gère l\textquotesingle exécution de plusieurs
  threads pour effectuer plusieurs tâches simultanément.
\item
  \textbf{logging} : Utilisée pour l\textquotesingle enregistrement des
  événements, particulièrement utile pour le débogage.
\item
  \textbf{json} : Utilisée pour la manipulation des données JSON,
  souvent utilisées pour les échanges de données entre systèmes.
\item
  \textbf{time} : Fournit diverses fonctions pour manipuler le temps.
\item
  \textbf{collections.deque} : Fournit une structure de données de type
  file pour la gestion d\textquotesingle un tampon circulaire.
\item
  \textbf{queue} : Utilisée pour la gestion des files
  d\textquotesingle attente de manière thread-safe.
\end{itemize}

\begin{quote}
\textbf{Bibliothèques tierces :}

Ces bibliothèques doivent être installées séparément, car elles ne font
pas partie de la bibliothèque standard de Python3.
\end{quote}

\begin{itemize}
\item
  \textbf{cv2} (OpenCV) : Utilisée pour la capture, le traitement et
  l\textquotesingle affichage des images vidéo.
\item
  \textbf{numpy} : Utilisée pour la manipulation des tableaux et des
  matrices, souvent utilisée avec OpenCV pour le traitement
  d\textquotesingle image.
\item
  \textbf{pyaudio} : Permet la capture et la lecture de
  l\textquotesingle audio en temps réel.
\item
  \textbf{tkinter} : Interface graphique native de Python, utilisée pour
  créer la fenêtre principale et les différents composants de
  l\textquotesingle interface utilisateur.
\item
  \textbf{PIL (ou Pillow)} : Utilisée pour la manipulation des images,
  spécifiquement pour convertir les images OpenCV en format compatible
  avec Tkinter.
\end{itemize}

\subsection{2. Comment installer les bibliothèques nécessaires
:}\label{comment-installer-les-bibliothuxe8ques-nuxe9cessaires}

\begin{quote}
Il suffit de taper ceci sur le terminal~: sudo apt install pyhton3-`nom
de la bibliothèque'.

On ne peut guère utiliser «~pip install~» car travaillant sur un
Raspberry pi, l'environnement est traité en externe d'où l'importance
d'utiliser «~sudo~» qui fait une demande en tant qu'administrateur.
Voici ce qu'il faut écrire sur le terminal pour les installer~:
\end{quote}

sudo apt \textbf{update}\\
sudo apt install \textbf{python3}-opencv \textbf{python3}-numpy
\textbf{python3}-pyaudio \textbf{python3}-pil

\subsection{2.1 Détails des bibliothèques installées
:}\label{duxe9tails-des-bibliothuxe8ques-installuxe9es}

\begin{itemize}
\item
  \textbf{python3-opencv} : Installe OpenCV, qui est utilisé pour la
  capture et le traitement d\textquotesingle images et de vidéos.
\item
  \textbf{python3-numpy} : Installe NumPy, une bibliothèque utilisée
  pour la manipulation efficace des tableaux, matrices et opérations
  mathématiques.
\item
  \textbf{python3-pyaudio} : Installe PyAudio, nécessaire pour capturer
  et jouer de l\textquotesingle audio en temps réel.
\item
  \textbf{python3-pil} : Installe Pillow, qui est une bibliothèque pour
  la manipulation d\textquotesingle images. Notez que sur certaines
  distributions, elle est encore référencée comme python3-pil.
\end{itemize}

\section{Descriptif du code}\label{descriptif-du-code}

\begin{quote}
Le script implémente une interface utilisateur pour capturer et diffuser
de la vidéo et de l\textquotesingle audio entre deux Raspberry Pi. Il
inclut aussi un système de chat textuel et une fonctionnalité
d\textquotesingle alerte. Voici un descriptif détaillé de la structure
du code et des points importants.
\end{quote}

\subsection{1. Importation des
Bibliothèques}\label{importation-des-bibliothuxe8ques}

\begin{quote}
Le script commence par importer les bibliothèques nécessaires :
\end{quote}

\begin{itemize}
\item
  \textbf{cv2 (OpenCV)} : Pour la capture et le traitement des vidéos.
\item
  \textbf{numpy} : Pour manipuler les données numériques sous forme de
  tableaux.
\item
  \textbf{pyaudio} : Pour la capture et la lecture de
  l\textquotesingle audio en temps réel.
\item
  \textbf{socket} : Pour la communication réseau via des sockets UDP.
\item
  \textbf{struct} : Pour la manipulation des données binaires.
\item
  \textbf{tkinter et PIL (Pillow)} : Pour créer
  l\textquotesingle interface graphique (GUI).
\item
  \textbf{threading et queue} : Pour gérer le multitâche et la
  communication inter-thread.
\item
  \textbf{logging} : Pour enregistrer les événements importants et les
  erreurs.
\item
  \textbf{json} : Pour manipuler les données au format JSON, utilisées
  pour les commandes entre les Raspberry Pi.
\end{itemize}

\subsection{2. Configuration des
Paramètres}\label{configuration-des-paramuxe8tres}

\begin{quote}
Le script définit plusieurs variables globales et constantes utilisées
tout au long du code :
\end{quote}

\begin{itemize}
\item
  \textbf{Dimensions de la vidéo (VIDEO\_WIDTH, VIDEO\_HEIGHT,
  FRAME\_SIZE)} : Définissent la taille des vidéos capturées et
  affichées.
\item
  \textbf{Paramètres audio (CHUNK, FORMAT, CHANNELS, RATE)} : Spécifient
  la configuration pour la capture et la lecture audio.
\item
  \textbf{Adresses IP et ports (REMOTE\_IP, SECONDARY\_IP, VIDEO\_PORT,
  AUDIO\_PORT, COMMAND\_PORT)} : Configurent la communication réseau
  entre les deux Raspberry Pi.
\item
  \textbf{Variables de contrôle (stop\_video\_event,
  stop\_secondary\_video\_event, stop\_audio\_event)} : Utilisées pour
  gérer l\textquotesingle arrêt des threads de capture/lecture audio et
  vidéo.
\item
  \textbf{Tampons vidéo et audio (video\_buffer, audio\_buffer)} :
  Stockent temporairement les données audios et vidéo reçues.
\end{itemize}

\subsection{3. Fonctions Principales}\label{fonctions-principales}

\subsubsection{a. Capture et Diffusion
Vidéo}\label{a.-capture-et-diffusion-viduxe9o}

\begin{itemize}
\item
  \textbf{send\_video()} : Capture les images de la caméra locale, les
  redimensionne, et les envoie par paquets via UDP à
  l\textquotesingle autre Raspberry Pi.
\item
  \textbf{receive\_video\_from\_secondary()} : Reçoit des segments vidéo
  de l\textquotesingle autre Raspberry Pi, les réassemble, puis les
  affiche via l\textquotesingle interface Tkinter.
\end{itemize}

\subsubsection{b. Capture et Diffusion
Audio}\label{b.-capture-et-diffusion-audio}

\begin{itemize}
\item
  \textbf{send\_audio()} : Capture l\textquotesingle audio depuis un
  microphone et l\textquotesingle envoie à l\textquotesingle autre
  Raspberry Pi via UDP.
\item
  \textbf{receive\_audio()} : Reçoit des données audio, ajuste le
  volume, et les joue via les haut-parleurs.
\end{itemize}

\subsubsection{c. Gestion des Commandes}\label{c.-gestion-des-commandes}

\begin{itemize}
\item
  \textbf{send\_command(command)} : Envoie des commandes sous forme de
  messages JSON à l\textquotesingle autre Raspberry Pi, comme démarrer
  ou arrêter la vidéo/audio.
\item
  \textbf{receive\_command()} : Écoute et traite les commandes reçues de
  l\textquotesingle autre Raspberry Pi, comme afficher une alerte ou
  recevoir un message de chat.
\end{itemize}

\subsubsection{d. Interface Utilisateur
(Tkinter)}\label{d.-interface-utilisateur-tkinter}

\begin{itemize}
\item
  \textbf{toggle\_my\_camera()} et \textbf{toggle\_secondary\_camera()}
  : Permettent à l\textquotesingle utilisateur de démarrer ou
  d\textquotesingle arrêter la capture vidéo sur l\textquotesingle un ou
  l\textquotesingle autre des Raspberry Pi.
\item
  \textbf{toggle\_audio()} : Permet à l\textquotesingle utilisateur de
  démarrer ou d\textquotesingle arrêter la capture audio.
\item
  \textbf{adjust\_volume(val)} : Ajuste le volume de la lecture audio.
\item
  \textbf{send\_chat\_message()} et
  \textbf{receive\_chat\_message(command)} : Gèrent
  l\textquotesingle envoi et la réception de messages de chat entre les
  deux Raspberry Pi.
\item
  \textbf{show\_alert()} : Affiche un message d\textquotesingle alerte
  en plein écran.
\end{itemize}

\subsection{4. Gestion des Threads}\label{gestion-des-threads}

\begin{itemize}
\item
  Le script utilise des threads pour exécuter simultanément la
  capture/lecture vidéo et audio, ainsi que pour écouter les commandes
  reçues. Cela permet à l\textquotesingle interface graphique de rester
  réactive pendant que les opérations réseau et multimédia sont
  effectuées en arrière-plan.
\end{itemize}

\subsection{5. Boucle Principale de
l\textquotesingle Interface}\label{boucle-principale-de-linterface}

\begin{itemize}
\item
  \textbf{root.mainloop()} : Lancement de la boucle principale de
  Tkinter, qui gère les événements de l\textquotesingle interface
  utilisateur.
\end{itemize}

\begin{quote}
\textbf{Points Importants}
\end{quote}

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  \textbf{Multithreading} : Le script utilise le multithreading pour
  gérer simultanément la capture/lecture de la vidéo, de
  l\textquotesingle audio, et l\textquotesingle écoute des commandes.
  Cela permet d\textquotesingle éviter que l\textquotesingle interface
  utilisateur se bloque lors de l\textquotesingle exécution de ces
  tâches en arrière-plan.
\item
  \textbf{Communication Réseau via UDP} : Le choix d\textquotesingle UDP
  pour la transmission des vidéos et de l\textquotesingle audio est
  crucial pour minimiser la latence. Cependant, il faut noter que UDP ne
  garantit pas la livraison des paquets, ce qui pourrait entraîner des
  pertes de données vidéo/audio.
\item
  \textbf{Tampons Circulaires} : Les tampons circulaires (comme
  audio\_buffer) sont utilisés pour lisser la lecture audio en cas de
  petites interruptions dans la réception des paquets, aidant à éviter
  les coupures audios.
\item
  \textbf{Interface Utilisateur} : Tkinter est utilisé pour créer une
  interface utilisateur simple mais fonctionnelle, permettant aux
  utilisateurs de contrôler facilement les flux vidéo et audio, ainsi
  que d\textquotesingle envoyer/recevoir des messages de chat.
\item
  \textbf{Volume Audio} : Le script inclut une fonctionnalité de
  contrôle du volume, ce qui est essentiel pour ajuster la lecture audio
  selon les besoins des utilisateurs.
\end{enumerate}

\section{Explication de la Connexion entre les Deux Raspberry
Pi}\label{explication-de-la-connexion-entre-les-deux-raspberry-pi}

\begin{quote}
La connexion des deux Raspberry Pi se fait via un réseau Wi-Fi local ou
par Ethernet, avec un Raspberry Pi principal qui gère
l\textquotesingle interface administrateur (y compris les commandes) et
un Raspberry Pi secondaire qui interagit avec le premier pour la capture
et la diffusion de l\textquotesingle audio, de la vidéo, et des messages
de chat. Voici une explication détaillée de cette connexion.
\end{quote}

\subsection{1. Configuration du Réseau Wi-Fi
Local}\label{configuration-du-ruxe9seau-wi-fi-local}

\begin{itemize}
\item
  \textbf{Raspberry Pi Principal (Serveur/Admin)} : Ce Raspberry Pi crée
  un point d\textquotesingle accès Wi-Fi local, auquel le deuxième
  Raspberry Pi se connecte. Ce Raspberry Pi est aussi celui qui exécute
  le code de gestion de l\textquotesingle interface utilisateur,
  permettant à l\textquotesingle utilisateur de contrôler les flux
  vidéo, audio et les commandes via une interface graphique (Tkinter).
\item
  \textbf{Raspberry Pi Secondaire (Client)} : Ce Raspberry Pi se
  connecte au réseau Wi-Fi local créé par le Raspberry Pi principal. Il
  envoie et reçoit des flux audio et vidéo selon les commandes reçues du
  Raspberry Pi principal.
\end{itemize}

\begin{quote}
Il faut nécessairement alors connectés les Raspberry pi au même wifi.

Dans le fichier du script nommé «~PicomAdmin/Client.py~», effacer
l'hashtag correspond au type de connexion que vous utilisé sur la
variable nommé «~REMOTE\_IP~». Une adresse IP correspondant à une
connexion WI-FI est attribuée par défaut, idem pour l'Ethernet. Ces
adresse IP reste donc inchangé sauf sur une migration de l'application
sur un autre appareil.

Si aucun wifi local n'a été créer, il est possible d'en crée 1 en
accédant au paramètre wifi via la barre latérale, puis aller à
«~Advanced Options~» enfin «~Create Wi-Fi Hotspot\ldots~». Vous aurez le
choix d'émettre un mot de passe ou non mais si c'est le cas, utiliser la
sécurité Wi-Fi «~WPA et WPA2 personnel~» pour qu'il soit détectable.
Lier à un nouveau Wi-Fi, l'adresse IP changera. Il est alors nécessaire
de modifier dans le script l'adresse IP de REMOTE\_IP. L'adresse IP des
Raspberry pi sont visible en glissant la souris sur le logo WI-FI sur la
barre latérale.
\end{quote}

\subsection{\texorpdfstring{2. Configuration du Réseau Ethernet
}{2. Configuration du Réseau Ethernet }}\label{configuration-du-ruxe9seau-ethernet}

\begin{quote}
Concernant la connexion Ethernet, il suffit de brancher un câble
Ethernet entre les deux Raspberry pi. Après cela il faut attendre 1 à 2
min pour que le Raspberry pi trouve l'IP correspondant au script. Pour
savoir si les Raspberry pi sont connectés, un logo de deux flèches
bleues dans un sens vertical opposé serra visible. Dans le cas
contraire, elles seront grises avec des croix rouges. Ils se peut
qu'après avoir débranché ou rebranché le câble Ethernet, cette liaison
et de recherche de l'adresse IP ne s'effectue pas. Il faut alors
redémarrer celui qui n'est pas connecté, ou redémarrer les deux
Raspberry pi en même temps puis rebranché les deux câbles.
\end{quote}

\subsection{3. Communication entre les Deux Raspberry
Pi}\label{communication-entre-les-deux-raspberry-pi}

\begin{quote}
La communication entre les deux Raspberry Pi se fait via des sockets
UDP, une méthode de transmission rapide mais non sécurisée qui convient
bien aux flux en temps réel comme la vidéo et l\textquotesingle audio.
Voici comment cette communication est organisée :
\end{quote}

\begin{itemize}
\item
  \textbf{Adresses IP et Ports} :

  \begin{itemize}
  \item
    \textbf{REMOTE\_IP} : C\textquotesingle est
    l\textquotesingle adresse IP du Raspberry Pi secondaire telle
    qu\textquotesingle elle est vue par le Raspberry Pi principal. Dans
    notre cas, c\textquotesingle est 10.42.0.147.
  \item
    \textbf{SECONDARY\_IP} : Adresse IP que vous utiliserez si vous
    souhaitez différencier les rôles des Raspberry Pi dans le réseau
    s'il y a plusieurs Raspberry pi connecté.
  \item
    \textbf{Ports (VIDEO\_PORT, AUDIO\_PORT, COMMAND\_PORT)} : Trois
    ports différents sont utilisés pour transmettre la vidéo,
    l\textquotesingle audio, et les commandes respectivement. Cela
    permet de segmenter les types de données échangées, réduisant ainsi
    les risques de collisions et facilitant la gestion des flux.
  \end{itemize}
\item
  \textbf{Transmission Vidéo} :

  \begin{itemize}
  \item
    \textbf{Envoi de Vidéo (send\_video())} : Le Raspberry Pi principal
    capture la vidéo via sa caméra, puis envoie les segments vidéo au
    Raspberry Pi secondaire via le port UDP spécifié. Les segments sont
    ensuite réassemblés pour être affichés.
  \item
    \textbf{Réception de Vidéo (receive\_video\_from\_secondary())} : Le
    Raspberry Pi principal peut aussi recevoir des flux vidéo du
    Raspberry Pi secondaire, si configuré ainsi. Ces segments vidéo sont
    reçus, réassemblés, et affichés via l\textquotesingle interface
    utilisateur.
  \end{itemize}
\item
  \textbf{Transmission Audio} :

  \begin{itemize}
  \item
    \textbf{Envoi d\textquotesingle Audio (send\_audio())} : Le
    Raspberry Pi principal capture l\textquotesingle audio en temps réel
    via un microphone, puis envoie les données audio au Raspberry Pi
    secondaire via un port UDP.
  \item
    \textbf{Réception d\textquotesingle Audio (receive\_audio())} : Le
    Raspberry Pi principal peut recevoir des flux audio du Raspberry Pi
    secondaire. Les données sont reçues, ajustées en volume, puis
    jouées.
  \end{itemize}
\item
  \textbf{Gestion des Commandes} :

  \begin{itemize}
  \item
    \textbf{Envoi de Commandes (send\_command())} : Le Raspberry Pi
    principal envoie des commandes au Raspberry Pi secondaire sous forme
    de messages JSON, pour contrôler des actions comme démarrer ou
    arrêter la capture vidéo/audio, ou encore afficher des alertes.
  \item
    \textbf{Réception de Commandes (receive\_command())} : Le Raspberry
    Pi principal écoute en permanence les commandes provenant du
    Raspberry Pi secondaire, et exécute les actions correspondantes.
  \end{itemize}
\end{itemize}

\subsection{4. Fonctionnement de l\textquotesingle Interface
Administrateur}\label{fonctionnement-de-linterface-administrateur}

\begin{itemize}
\item
  \textbf{Raspberry Pi Principal} : L\textquotesingle interface
  utilisateur permet de contrôler l\textquotesingle ensemble du système.
  L\textquotesingle utilisateur peut démarrer ou arrêter les flux
  vidéo/audio, envoyer des commandes au Raspberry Pi secondaire, et
  afficher des messages de chat. C\textquotesingle est le centre de
  contrôle, ce qui fait de ce Raspberry Pi
  l\textquotesingle administrateur du réseau.
\item
  \textbf{Raspberry Pi Secondaire} : Ce Raspberry Pi exécute les
  commandes envoyées par le Raspberry Pi principal, telles que démarrer
  la capture vidéo ou audio. Il n\textquotesingle a pas
  d\textquotesingle interface utilisateur, il est principalement un
  exécutant des instructions reçues.
\end{itemize}

\begin{quote}
Un fichier nommé «~config.json~» à été créer pour permettre a un
utilisateur de référer dans ce fichier l'adresse correspondant sans
ouvrir le script.
\end{quote}

\section{Installation OS et Emplacement du
code}\label{installation-os-et-emplacement-du-code}

Utiliser l'application «~Raspberry pi Imager~» pour pouvoir formater et
installer l'os de son choix, par rapport à la version de son Raspberry
pi. Un lien est disponible pour plus d'information~:

\url{https://www.raspberrypi.com/software}

Concernant le code, il faut se rendre Dans~:
/Documents/Picom/PicomAdmin.py

Dans le fichier Picom vous pourriez y voir un fichier nommé
«~start\_app.sh~» qui permet lancer le code sans éditeur de texte. Un
autre fichier dans le répertoire Desktop permet via le biais de
«~start\_app.sh~» et une image pour l'afficher en raccourci et exécuter
dès le bureau.

\section{Astuce}\label{astuce}

\textbf{1.Copier les données de la carte SD}

Il y a la possibilité de copier l'intégralité des fichiers et données
d'une carte SD et de la transférer à un autre. Cela permettra d'exécuter
l'application sans réaliser les étapes émises plus haut. Pour cela
utiliser SD-Card Copier, une application intégrer au Raspberry pi qui
permet de faire ce travail.

\end{document}
