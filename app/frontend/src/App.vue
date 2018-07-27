<template>
    <div>
        <navbar v-bind:logged_in="logged_in" @user_login_state="set_login"/>
        <goals v-bind:macro_goals="macro_goals" v-bind:today_meals='today_meals'/>
        <div class='container'>
            <div class="row">
                <div class="six columns half-height">
                    <day_summary v-bind:today_meals="today_meals" v-bind:foods="foods" @refresh_meals='getMeals' @refresh_foods='getFoods'/>
                </div>
                <div class="six columns half-height">
                    <weight_log ref="weight_log"/>
                </div>
            </div>
            <div class="row">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import navbar from './components/navbar.vue'
import goals from './components/goals.vue'
import day_summary from './components/day_summary.vue'
import weight_log from './components/weight_log.vue'
import 'raleway-webfont/raleway.min.css'
import 'skeleton-css/css/skeleton.css'

export default {
    data: function () {
        return {
            today_meals: [],
            foods: [],
            macro_goals: {
                cal: 5000,
                car: 600,
                fat: 227,
                pro: 225
            },
            logged_in: false
        }
    },
    components: {
        navbar,
        goals,
        day_summary,
        weight_log
    },
    methods: {
        set_login: function (state) {
            this.logged_in = state;
            if (state){
                this.getMeals();
                this.getFoods();
                this.$refs.weight_log.getWeightLog();
            }
        },
        getFoods: function () {
            axios.post('http://localhost:5000/api/getfoods', {}, {withCredentials: true}
                ).then(response => {
                    this.foods = response.data;
                }).catch(error => {
                    console.log(error);
                });
        },
        getMeals: function () {
            axios.post('http://localhost:5000/api/getmeals', {}, {withCredentials: true}
                ).then(response => {
                    this.today_meals = response.data;
                }).catch(error => {
                    console.log(error);
                });
        },
        getFoods: function () {
            axios.post('http://localhost:5000/api/getfoods', {}, {withCredentials: true}
                ).then(response => {
                    this.foods = response.data;
                }).catch(error => {
                    console.log(error);
                });
        }
    }
}
</script>
