var animals = [
    {% for ownanimal in farm.ownanimal_set.all %}
        {
            species: "{{ ownanimal.animal.species }}",
            breed:  "{{ ownanimal.animal.breed }}",
            nr_owned: "{{ ownanimal.nr_owned }}"
            buy_price: "{{ownanimal.animal.buy_price }}"
            sell_price: "{{ownanimal.animal.sell_price"
        }
    {% endfor %}
]