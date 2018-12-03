//var leboncoinApi = require("leboncoin-api")
var iconv = require('iconv-lite');
// Load the full build of lodash
var _ = require('lodash');
const leboncoin = require('leboncoin-api');

function newSearch(pageNo) {
	let search = new leboncoin.Search({page: pageNo})
		//.setPage(1)
		.setQuery("")
		.setFilter(leboncoin.FILTERS.ALL)
		.setCategory("ventes_immobilieres")
		.setRegion("ile_de_france")
	 
		.addSearchExtra("price", {min: 0, max: 1000000}) // "Plus de 2000"
	return (search);
}

// Change this number to limit the number of pages that are returned
var pageLimit = 150;

var search = newSearch(1);

search.run().then(function (d) {
		pageLimit = d.pages;
	}, function (err) {
		console.log(err);
	}
);

queries = [ ];
for (let i = 0; i < pageLimit; i++){
	queries[i] = newSearch(i + 1);
}

//console.log("number of queries" + queries.length);
var res = 0;
for (i = 0; i < queries.length; i++)
{
	queries[i].run().then(function success(data) {
		//console.log(data.pages); // the number of pages
		//console.log(data.nbResult); // the number of results for this search
		//console.log("result: " + data.page + " out of " + data.pages);
		//console.log(data.results); // the array of results
		for (i = 0; i < data.results.length; i++){
			zip = data.results[i].location.zipcode;
			if (zip[0] == '7' && zip[1] == '5'){
				console.log(data.results[i]);
				//console.log("total" + res);
				res++;
			}
		}
	}, function (err) {
		console.error(err);
	});
}

