# pdfsam Softwareentwicklung - feature #84

**Getting Startet:**

*Schritt für Schritt zum starten der Entwicklungsumgebung*

 - [ ] IntelliJ IDEA Community Edition 14.1.4
 - [ ] Java Main-Methode finden. *Suche öffnen:* <kbd>SHIFT</kbd><kbd>SHIFT</kbd> -> `main`


**09.07.2015 - Getting Startet:**

 - [ ] Der Unit-Test `contextMenuReplacesText` wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?)
 Datei: `X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java`
 - [ ] Parent Pom wird nicht gefunden beim starten der pdfsam-community variante. (`mvn exec:java`). Weiterer Schritt nötig um Parent Pom lokal zu installieren: `cd pdfsam-parent && mvn install`, bevor pdfsam-community gestartet werden kann.
 - [ ] Neuer vollständiger Befehl um das Projekt zu bauen, im lokalen maven repository zu installieren und pdf-sam community zu starten: `mvn clean install -Dmaven.test.skip=true && cd pdfsam-parent/ && mvn install && cd .. && cd pdfsam-community && mvn exec:java`
 
**14.07.2015 - Getting Startet:**

 - [ ] Main Methode finden. *Suche öffnen:* <kbd>SHIFT</kbd><kbd>SHIFT</kbd> -> `main`
 - [ ] Workspace Klassen finden. *Suche öffnen:* <kbd>SHIFT</kbd><kbd>SHIFT</kbd> -> `Workspace`
 - [ ] Maven Projekt Starten und Debuggen. *Window: Maven Projects* -> `PDFsam Community Edition application` -> *Plugins* -> *exec* -> *exec:java* -> Rechte Maustaste -> *Create ...* ( [#1](https://www.jetbrains.com/idea/help/creating-maven-run-debug-configuration.html) ). Dann kann man mit `Run ...` oder `Debug ...` die Anwendung ausführen oder debuggen.
 - [ ] Starter (Run.../Debug...) so anpassen das Kommandozeilen Optionen mit angegeben werden. *Command line:* `exec:java -Dexec.args=-h` *Name:* `pdfsam-community [exec:java -Dexec.args="-h"] `.
 - [ ] Übergabe des Kommandozeilenparameters überprüfen. *Debug...* -> *Klasse: `org.pdfsam.community.App`* -> Breakpoint innerhalb der Main-Methode. Parameter `args` überprüfen ob `-h` enthalten ist.

`mvn clean install -Dmaven.test.skip=true && cd pdfsam-parent/ && mvn install && cd .. && cd pdfsam-community && mvn exec:java`

*Vorgehen*

 - [ ] Main-Methode auf Kommandozeilen Optionen überprüfen.
 - [ ] Gibt es schon Kommandoteilen Parameter?
 - [ ] Gibt es schon eine Logik für Kommandozeilen Parameter?
       + Ja, Klasse `ParametersImpl`.
       + [org.pdfsam.PdfsamApp Zeile 107-114](https://github.com/tobiashochguertel/pdfsam/blob/feature-84/pdfsam-gui/src/main/java/org/pdfsam/PdfsamApp.java#L107-114)
 - [ ] Kommandozeilen Hilfe `-h` planen.
 - [ ] Unit-Test für den Kommandozeilen `-h` programmieren.
 - [ ] Kommandozeilen Hilfe `-h` programmieren.
 - [ ] Methode finden, die eine Workspace Datei lädt.
 - [ ] Methode finden, die eine geladenen Workspace Sitzung ausführt (Run).
 - [ ] Unit-Test für den Kommandozeilen `--workspace-file` planen. (Liste mit Tests)
 - [ ] Unit-Test für den Kommandozeilen `--workspace-file` programmieren.
 - [ ] Main-Methode um Kommandozeilen Parameter `--workspace-file <file> Absolute Path to an existing workspace file.` erweitern.
