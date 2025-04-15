# IVG
Dati sull'interruzione volontaria di gravidanza in Italia aggiornati al 2023

Sul portale Epicentro, l'Istituto superiore di sanità ha pubblicato i dati relativi agli ospedali nei quali viene effettuata l'interruzione volontaria di gravidanza. Oltre all'elenco dei centri con il relativo indirizzo, i dati fanno riferimento al numero di IVG farmacologiche e non farmacologiche eseguite e alla distribuzione percentuale della settimana alla quale è stata portata a termine l'interruzione. I dati si trovano a questo link: https://www.epicentro.iss.it/ivg/progetto-ccm-2022-mappa-punti-ivg

Data la difficoltà nel reperire questi dati (per chi fosse interessato, consiglio la lettura di 'Mai dati', libro inchiesta di Chiara Lalli e Sonia Montegiove) e visto che sul portale Epicentro non è possibile scaricarli in formato aperto, dopo aver usato questi dati per un articolo uscito su Wired Italia, ho pensato di aprirli e renderli disponibili. Più nel dettaglio:

-Il file IGV_Raw.csv contiene i dati grezzi così come li ho estratti utilizzando la funzione ImportHtml di Google Sheet

-Il file IGV_Geocoded.csv contiene i dati puliti e geocodificati

-Il file IVGgeocoded.py contiene il codice (emendato del percorso dei file e dell'API Key di Here Maps) scritto con ChatGPT-4o per geocodificare gli indirizzi degli ospedali e delle strutture sanitarie
