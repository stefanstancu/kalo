<template>
    <div>
        <h2>Today</h2>
        <div id='wrapper'>
            <table>
            <thead>
                <tr>
                    <th>Meal Name</th>
                    <th>Date</th>
                    <th>Calories</th>
                    <th>Carbs</th>
                    <th>Fat</th>
                    <th>Protein</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="meal in today_meals">
                    <td>{{meal.name}}</td>
                    <td>{{meal.timestamp}}</td>
                    <td>{{meal.calories}}</td>
                    <td>{{meal.carbohydrates}}</td>
                    <td>{{meal.fat}}</td>
                    <td>{{meal.protein}}</td>
                </tr>
            </tbody>
            </table>
        </div>
        <button @click='showAddMeal = true' class='button-primary'>Add Meal</button>
        <modal v-if='showAddMeal' @close='showAddMeal=false'>
            <add_meal v-bind:foods="foods" slot='body' @refresh_food="$emit('refresh_food')" @refresh_meals="$emit('refresh_meals')"/>
        </modal>
    </div>
</template>

<style scoped>
    h2 {
        text-align:center;
    }
    table {
        overflow-y:auto;
        font-size: 0.8em;
        width:100%;
    }

    div {
        height: 100%;
    }

    #wrapper {
        height: 90%;
        overflow-y: auto;
    }
</style>

<script>
import modal from './modal.vue'
import add_meal from './add_meal.vue'

export default {
    props: ['today_meals', 'foods'],
    data: function () {
        return {
            showAddMeal: false
        }
    },
    components: {
        modal,
        add_meal
    },
    methods: {
    }
}
</script>
