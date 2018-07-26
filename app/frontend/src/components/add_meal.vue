<template>
    <div class="row">
        <div class="six columns">
            <h4>New Meal Entry</h4>
            <form>
                <div class="row">
                    <label class="six columns">Meal Name</label>   
                    <label class="six columns">Date</label>   
                </div>
                <div class="row">
                    <input class="six columns" type="text" name="Meal Name" placeholder="New Meal" v-model="meal.name"/>
                    <input class="six columns" type="date" v-model="meal.date"/>
                </div>
                <div class="row">
                        <label class="six columns">Food Item</label>
                        <label class="three columns">Amount</label>
                </div>
                <div class="row" v-for="(item, index) in meal.items">
                        <input class="six columns" type="text" list="item_name" v-model="item.name"/>
                        <input class="three columns" type="number" v-model="item.amount"/>
                            <button @click="removeItem(index)" class="button u-pull-right" type="button">x</button>
                </div>
                <datalist id="item_name">
                    <option v-for="food in foods">{{food.name}}</option>
                </datalist>
                <div class="row">
                    <button @click="addItem" type="button" class="button u-full-width"><p style="font-size:4em">+</p></button>
                </div>
                <div class="row">
                    <button @click="saveMeal" type="button" class="button u-full-width">SAVE</button>
                </div>
            </form>
            <div v-show="mealErrors.length > 0">
                Whoops! We've found some errors in your meal.
                <hr>
                <ul>
                    <li v-for="error in mealErrors">
                        {{error}}
                    </li>
                </ul>
            </div>
            <p v-show="saveMealResponse != 0">{{saveMealResponse}}</p>
        </div>
        <div class="six columns">
            <p v-show="saveResponse != 0"> {{saveResponse}}</p>
            <div class="row">
                <h4 class="six columns">My Food  <span style="font-size: 0.6em">(/100g)</span></h4>
                <div class="three columns">
                    <button @click="toggle_save_food" class="button" type="button">{{show_save_food?"cancel":"custom"}}</button>
                </div>
                <div class="three columns">
                    <button @click="toggle_search_food" class="button" type="button">{{show_search_food?"cancel":"search"}}</button>
                </div>
            </div>
            <div v-show="show_save_food">
                <h4>Food Item</h4>
                <form>
                    <div class="row">
                            <label for="name_input">Name</label>
                            <input class="u-full-width" id="name_input" type="text" v-model="food.name"/>
                    </div>
                    <div class="row">
                        <div class="eight columns">
                            <label for="measure_input">Serving size</label>
                            <input class="u-full-width" id="measure_input" type="number" v-model="food.measure"/>
                        </div>
                        <div class="four columns">
                            <label for="unit_input">Unit </label>
                            <select class="u-full-width" id="unit_input" v-model="food.unit">
                                <option value="g">g</option>
                            </select>
                        </div>
                    </div>
                    <div class="row">
                        <div class="six columns">
                            <label style="padding-bottom: 7px; padding-top: 7px; margin-bottom: 15px; border: 1px;" for="calories_input">Calories</label>
                            <label style="padding-bottom: 7px; padding-top: 7px; margin-bottom: 15px; border: 1px;" for="carbs_input">Carbohydrates</label>
                            <label style="padding-bottom: 7px; padding-top: 7px; margin-bottom: 15px; border: 1px;" for="fats_input">Fats</label>
                            <label style="padding-bottom: 7px; padding-top: 7px; margin-bottom: 15px; border: 1px;" for="protein_input">Protein</label>
                        </div>
                        <div class="six columns">
                            <input class="u-full-width" id="calories_input" type="number" v-model="food.calories"/>
                            <input class="u-full-width" id="carbs_input" type="number" v-model="food.carbohydrates"/>
                            <input class="u-full-width" id="fats_input" type="number" v-model="food.fat"/>
                            <input class="u-full-width" id="protein_input" type="number" v-model="food.protein"/>
                        </div>
                    </div>
                    <div class="row">
                            <button @click="sendFood(food)" type="button" class="button u-pull-right">SAVE</button>
                    </div>
                </form>
            </div>
            <div v-show="foodErrors.length > 0">
                Darn! We've found some errors in your food item.
                <hr>
                <ul>
                    <li v-for="error in foodErrors">
                        {{error}}
                    </li>
                </ul>
            </div>
            <div v-show="show_search_food">
                <div class="row">
                    <p> Data provided by the USDA Nutrition Database </p>
                    <input v-model="food_query" class="u-full-width" id="food_query" type="text"/>
                </div>
                <div class="row"><b>
                    <div class="seven columns" > Name </div>
                    <div class="one columns"> Cal </div>
                    <div class="one columns"> Car </div>
                    <div class="one columns"> Fat </div>
                    <div class="one columns"> Pro </div>
                    <div class="one column"> &nbsp </div>
                    </b>
                </div>
                <div v-for="(food, index) in search_results">
                    <div class="row" @mouseover="showSaveFood = index" @mouseleave="showSaveFood = -1">
                        <div class="seven columns" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"> {{food.name}} </div>
                        <div class="one columns"> {{food.calories}} </div>
                        <div class="one columns"> {{food.carbohydrates}} </div>
                        <div class="one columns"> {{food.fat}} </div>
                        <div class="one columns"> {{food.protein}} </div>
                    </div>
                </div>
                <hr>
            </div>
            <div>
                <div class="row"><b>
                    <div class="seven columns" > Name </div>
                    <div class="one columns"> Cal </div>
                    <div class="one columns"> Car </div>
                    <div class="one columns"> Fat </div>
                    <div class="one columns"> Pro </div>
                    <div class="one column"> &nbsp </div>
                    </b>
                </div>
                <div style="overflow: auto; height: 200px;">
                    <div v-for="(food, index) in foods">
                        <div class="row" @mouseover="showRemoveFood = index" @mouseleave="showRemoveFood = -1">  
                            <div class="seven columns" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"> {{food.name}} </div>
                            <div class="one columns"> {{Math.round(food.calories/food.measure*100)}} </div>
                            <div class="one columns"> {{Math.round(food.carbohydrates/food.measure*100)}} </div>
                            <div class="one columns"> {{Math.round(food.fat/food.measure*100)}} </div>
                            <div class="one columns"> {{Math.round(food.protein/food.measure*100)}} </div>
                            <a href="#" @click="removeFood(index)" v-show="showRemoveFood == index" class="one column" style="text-decoration: none;">x</a>
                        </div>
                    </div>
                    <div style="text-align:center; padding: 5%" v-show="foods.length == 0">
                        Start by adding some food items. <br> Then you can track meals composed of your food!
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['foods'],
        data: function () {
            return {
                food: {
                    name: '',
                    measure: "",
                    unit: '',
                    calories: "",
                    carbohydrates: "",
                    fat: "",
                    protein: ""
                },
                meal: {name:"", date:"", items: [{name:"", amount:0}]},
                meals: [],
                search_results: [],
                user_name: "",
                saveResponse: 0,
                saveMealResponse:0,
                food_query: "",
                food_query_timer_id: "",
                show_table: true,
                show_save_food: false,
                show_search_food: false,
                mealMenuShow: -1,
                showRemoveFood: -1,
                showSaveFood: -1,
                mealErrors: [],
                foodErrors: [],
                loggedIn: false
            }
        },
        watch: {
            food_query: function(new_value, old_value) {
                clearTimeout(this.food_query_timer_id);
                this.food_query_timer_id = setTimeout(function () {
                    if (new_value == "") { return; }
                    axios.post('http://localhost:5000/api/querydb', {query:new_value}, {withCredentials: true}
                    ).then(response => {
                        search_results = response.data;
                    }).catch(error => {
                        console.log(error);
                    });
                }, 350);
            }
        },
        methods: {
            toggle_save_food: function () {
                this.show_save_food = !this.show_save_food;
            },
            toggle_search_food: function () {
                this.show_search_food = !this.show_search_food;
            },
            sendFood: function (food) {
                if (!this.validateFood(food)){ return; }
                saveResponse = "loading...";
                axios.post('http://localhost:5000/api/savefood', food, {withCredentials: true}
                ).then(response => {
                    this.saveResponse = response.data;
                    this.$emit('refresh_food');
                    this.savefood = false;
                }).catch(error => {
                    console.log(error);
                });
            },
            saveMeal: function () {
                if (!this.validateMeal()){ return; }
                this.saveMealResp = "adding...";
                axios.post('http://localhost:5000/api/savemeal', this.meal, {withCredentials: true}
                ).then(response => {
                    this.saveMealResponse = response.data;
                    this.$emit('refresh_meals');
                    this.clearMeal();
                }).catch(error => {
                    console.log(error);
                });
            },
            removeMeal: function (index) {
                axios.post('http://localhost:5000/api/deletemeal', {id: this.meals[index].id}, {withCredentials: true}
                ).then(reposonse => {
                    this.getMeals();
                }).catch(error => {
                    console.log(error);
                });
            },
            removeFood: function (index) {
                axios.post('http://localhost:5000/api/deletefood', {id: this.foods[index].id}, {withCredentials: true}
                ).then(reposonse => {
                    this.getFoods();
                }).catch(error => {
                    console.log(error);
                });
            },
            validateMeal: function (){
                // Needs non-zero amount
                var food_names = [];
                for (var food of this.foods) {
                    food_names.push(food.name);
                }
                var errors = [];
                for (var food of this.meal.items){
                    if (!(food_names.includes(food.name))){
                        if (food.name == ""){
                            errors.push("Blank");
                        }
                        else {
                            errors.push(food.name);
                        }
                    }
                }
                if (errors.length == 1){
                    errors[0] = errors[0] + " is not a saved food";
                }
                else if (errors.length > 1) {
                    errors[0] = errors.reduce((total, next) => total + ", " + next);
                    errors = [errors[0] + " are not saved foods"];
                }
                if (this.meal.length < 0){
                    errors.push("You need at least 1 food item for a meal");
                }
                for (var food in this.meal.items){
                    if (this.meal.items[food].amount == 0){
                        errors.push("You need to have a non-zero food amount");
                        break;
                    }
                }
                if (this.meal.name == "") {
                    errors.push("You need to give your meal a name");
                }
                this.mealErrors = errors;
                return (errors.length == 0);
            },
            validateFood: function (food){
                // Needs all fields to be populated
                var errors = [];
                if (food.name == "") {
                    errors.push("Food name cannot be blank");
                }
                if (food.measure == "" || food.unit == "") {
                    errors.push("Measure cannot be blank");
                }
                if (food.calories === "" || food.carbohydrates === "" || food.fat === "" || food.protein === ""){
                    errors.push("Missing attribute value");
                }
                this.foodErrors = errors;
                return (errors.length == 0);
            },
            addItem: function() {
                var elem = document.createElement('div');
                this.meal.items.push({
                    name:"",
                    amount: 0
                });
            },
            removeItem: function (index) {
                this.meal.items.splice(index, 1);
            },
            clearMeal: function () {
                this.meal = {name:"", date:"", items: [{name:"", amount:0}]};
            }
        }
    }

</script>
