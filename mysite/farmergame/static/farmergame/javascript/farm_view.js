document.getElementById('all_data').innerHTML = "momen!"

var money = 300//{{ farm.capital }}
/*var animals = [
    {% for ownanimal in farm.ownanimal_set.all %}
        {
            species: "{{ ownanimal.animal.species }}",
            breed:  "{{ ownanimal.animal.breed }}",
            nrOwned: {{ ownanimal.nr_owned }},
            buyPrice: {{ownanimal.animal.buy_price }}.
            sellPrice: {{ownanimal.animal.sell_price}},
        }
    {% endfor %}
]

//var fields = {{ farm.fields }}*/