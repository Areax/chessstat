    const ChessTools = require('chess-tools');
	const ECO = ChessTools.ECO;
    const eco = new ECO();
    let pgn = "1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d3";
    eco.on("loaded", ()=>{ 
        let opening = eco.find(pgn);
        console.log("ECO CODE", opening.eco_code);
        console.log("NAME", opening.name);
        console.log("VARIATION", opening.variation);
        //See entry.js in the eco folder for more details.
    });
    eco.load_default(); //loads a default opening database (see sources below)
    //alternatively eco.load(stream) for a stream of a standard pgn file of openings.