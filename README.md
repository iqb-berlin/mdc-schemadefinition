# Metadaten als flexible Objekteigenschaften
In Anwendungen mit einigermaßen umfangreichen Datenstrukturen 
möchte man möglichst flexibel Objekteigenschaften speichern.
Außerdem möchte man über Anwendungsgrenzen hinweg Daten 
austauschen, ohne stets Beschreibungsdaten mitliefern zu
müssen. 

Das IQB verwendet Metadatenkataloge, in denen die
Metadaten definiert sind. Verschiedene Anwendungen greifen 
darauf zu und erzeugen auf dieser Grundlage Eingabeformulare
und Datenlisten usw. Jede Anwendung, die in importierten Daten
Verweise auf diese Kataloge entdeckt, kann die Daten korrekt
interpretieren.  

In diesem Repository sind die grundsätzlichen Definitionen zu
finden:
- mdc.xsd: Eine XML-Schemadatei, die die Syntax eines Katalogs
beschreibt
- mdc-vh.xsd: Eine XML-Schemadatei, die die Syntax eines Versionshistorie
 für einen Katalog beschreibt

# Begriffe
- Ein Metadatenkatalog MDC ist eine Sammlung von 
Metadatendefinitionen MDD. 
- Eine Metadatendefinition beschreibt den Typ und damit 
mögliche Werte für eine Information. Sie legt die Bedeutung der Werte in Bezug auf ein Datenobjekt fest und sichert so die Übertragbarkeit der Information über Systemgrenzen hinweg.
- Der Metadatenkatalog hat eine eindeutige ID.
- Metadatendefinitionen haben eine ID, die innerhalb des Katalogs eindeutig ist.
- Ein Metadatenkatalog kann selbst Metadaten enthalten, die über einen anderen Metadatenkatalog definiert sind.
- Eine Metadatendefinition kann selbst Metadaten enthalten, die über einen anderen Metadatenkatalog definiert sind.
# Versionierung
- Ein Metadatenkatalog wird nach dem SemVer-System MAJOR.MINOR.PATCH versioniert. Weder einzelne Metadatendefinitionen noch zulässige Werte innerhalb von Metadatendefinitionen werden versioniert.
- Sobald sich Inhalte des Metadatenkatalogs derart ändern, dass Dateninkompatibilität anzunehmen ist, wird die MAJOR -Versionsnummer erhöht. Es wird im Katalog eine Information „changelog“ hinterlegt, welche Metadatendefinition(en) betroffen sind/ist und welche Art die Änderung war (kurzer Text).
- Sobald neue Metadatendefinitionen zu einem Metadatenkatalog hinzugefügt wurden, wird die MINOR-Version erhöht.
- Die PATCH-Version wird erhöht, wenn kleinere Änderungen ohne Auswirkungen auf die existierenden Daten vorgenommen wurden.
- In einem Katalog ist ein Verweis zu finden zu einer XML-Datei, die die Änderungen beschreibt. Dadurch kann jede Anwendung einen Dialog anbieten, mit dem Objektmetadaten auf neuere Katalogversionen gehoben werden können.    
