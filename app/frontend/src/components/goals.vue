<template>
    <div>
        <div class='row'>
            <div class='four columns'>
                &nbsp;
            </div>
            <div class='eight columns'>
                <div class='three columns outline'>
                    <h3>Calories</h3>
                </div>
                <div class='three columns outline'>
                    <h3>Carbs</h3>
                </div>
                <div class='three columns outline'>
                    <h3>Fat</h3>
                </div>
                <div class='three columns outline'>
                    <h3>Protein</h3>
                </div>
            </div>
        </div>
        <div class='row'>
            <div class='four columns outline'>
                <h2>Goals</h2>
            </div>
            <div class='eight columns'>
                <div class='three columns outline'>
                    <b>{{macro_goals.cal}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.car}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.fat}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.pro}}</b>
                </div>
            </div>
        </div>
        <div class='row'>
            <div class='four columns outline'>
                <h2>Totals</h2>
            </div>
            <div class='eight columns'>
                <div class='three columns outline'>
                    <b>{{totals.cal}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{totals.car}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{totals.fat}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{totals.pro}}</b>
                </div>
            </div>
        </div>
        <div class='row'>
            <div class='four columns outline'>
                <h2>Remaining</h2>
            </div>
            <div class='eight columns'>
                <div class='three columns outline'>
                    <b>{{macro_goals.cal - totals.cal}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.car - totals.car}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.fat - totals.fat}}</b>
                </div>
                <div class='three columns outline'>
                    <b>{{macro_goals.pro - totals.pro}}</b>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: [
            'macro_goals',
            'today_meals'
        ],
        computed: {
            totals: function () {
                let totals = {
                    cal: [],
                    car: [],
                    pro: [],
                    fat: []
                };

                Object.entries(this.today_meals).forEach(([key, value])=> {
                    totals.cal.push(value.calories);
                    totals.car.push(value.carbohydrates);
                    totals.pro.push(value.protein);
                    totals.fat.push(value.fat);
                });
                totals.cal = totals.cal.reduce(function(total, num){ return total + num }, 0);
                totals.car = totals.car.reduce(function(total, num){ return total + num }, 0);
                totals.fat = totals.fat.reduce(function(total, num){ return total + num }, 0);
                totals.pro = totals.pro.reduce(function(total, num){ return total + num }, 0);
                return totals;
            }
        }
    }
</script>

<style scoped>
h3 {
    margin-bottom: 5px;
    font-size: 1.75rem;
}

.outline{
    border: 2px;
    border-style: solid;
    border-color: #f4f4f4;
    border-radius: 10px;
    text-align: center;
}

.container {
    border: 2px;
    margin-bottom: 20px;
}

</style>
