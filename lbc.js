var leboncoinApi = require("leboncoin-api")
var iconv = require('iconv-lite');
// Load the full build of lodash
var _ = require('lodash');

// merge objects
console.log(
    _.assign({ 'a': 1 }, { 'b': 2 }, { 'c': 3 })
)

// map an array
console.log(
    _.map([1, 2, 3], function(n) { return n * 3; })
)



const leboncoin = require('leboncoin-api');

function newSearch(pageNo) {
	let search = new leboncoin.Search({page: pageNo})
		//.setPage(1)
		.setQuery("renove")
		.setFilter(leboncoin.FILTERS.ALL)
		.setCategory("ventes_immobilieres")
		.setRegion("ile_de_france")
		.setDepartment("Paris")
	//    .setLocation([
	//                 {"zipcode": "78100"},
	//                 {"zipcode": "78000"},
	//                 ]) // Commented out .setLocation because it narrows down the search results too much
	 
		.addSearchExtra("price", {min: 0, max: 1000000}) // "Plus de 2000"
		.addSearchExtra('furnished', ["1", "Non meublé"]) // "label": "Meublé","value": "1","label": "Non meublé","value": "2"
	//    .addSearchExtra('real_estate_type', ["Maison", "Autre"]) // "label": "Maison","value": "1","label": "Appartement","value": "2","label": "Terrain","value": "3","label": "Parking","value": "4","label": "Autre","value": "5"
		.addSearchExtra('rooms', {min: 0, max: 8}) // "Plus de 8"
		.addSearchExtra('square', {min: 0, max: 300}) // "Plus de 300"
	//    .addSearchExtra('price', {min: 0, max: 1200}) // "Plus de 1200"
		.addSearchExtra('bedrooms', {min: 1, max: 6}) // "Plus de 6"
	//    .addSearchExtra('capacity', {min: 0, max: 12}) // "Plus de 12"
	//    .addSearchExtra('price', {min: 0, max: 4000}) // "Plus de 4000"
		.addSearchExtra('swimming_pool', ["1", "Non"])    
	//    .addSearchExtra('lease_type', ["Ventes", "rent"]) // "label":"Ventes","value":"sell","label":"Locations","value": "rent"
	//    .addSearchExtra('price', {min: 0, max: 500000}) // "Plus de 500 000"
	//    .addSearchExtra('price', {min: 0, max: 1000}) // "Plus de 1 000" "15"
	//    .addSearchExtra('price', {min: 0, max: 1000}) // "Plus de 1 000" "16"
	//    .addSearchExtra('price', {min: 0, max: 500}) // "Plus de 500" "17"
	//    .addSearchExtra('price', {min: 0, max: 1000}) // "Plus de 1000" "19"
	return (search);
}
// Please check into categories & sub categories constants to know which are the sub categories to add into "addSearchExtra"

// Change this number to limit the number of pages that are returned
let pageLimit = 164;

queries = [ ];

for (let i = 0; i < pageLimit; i++){
	queries[i] = newSearch(i + 1);
}

for (i = 0; i < queries.length; i++)
{
	queries[i].run().then(function success(data) {
		console.log(data.page + " out of " + data.pages); // the current page
		console.log(data.pages); // the number of pages
		console.log(data.nbResult); // the number of results for this search
		console.log(data.results); // the array of results
	}, function (err) {
		console.error(err);
	});
}
