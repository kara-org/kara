
// Use Parse.Cloud.define to define as many cloud functions as you want.
// For example:
Parse.Cloud.define("hello", (request) => {
	return "Hello world!";
});


Parse.Cloud.define("editarDemanda", async (request) => {
	
	let demandaAux = request.params.demanda;

	console.error(demandaAux);
	console.error(request);
	console.info(demandaAux);
	console.info(request);

	const query = new Parse.Query("Demanda");	
	const  demanda = await query.get(demandaAux.objectId);

	demanda.set('nome', demandaAux.nome);
    demanda.set('quantidadeAlcancada', demandaAux.quantidadeAlcancada);
    demanda.set('quantidadeDesejada', demandaAux.quantidadeDesejada);
    demanda.set('categoria', demandaAux.categoria);
	demanda.set('ativo', demandaAux.ativo);		
	await demanda.save()

	return demanda;
});