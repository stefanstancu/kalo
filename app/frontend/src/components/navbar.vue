<template>
    <div class="nav-bar container">
        <div class="row">
            <div class="six columns">
                <h1>Kalo</h1>
            </div>
            <div class="four columns">
                <div v-show='logged_in' class="username">
                {{username}}
                </div>
            </div>
            <div class="two columns">
                <button class='button-primary' @click='sign_out' v-show="logged_in">Sign Out</button>
                <g_signin_btn v-show='!logged_in' v-bind:logged_in="logged_in" @done_g_signin='sign_in'/>
            </div>
        </div>
        <div class="row">
            <hr>
        </div>
    </div>
</template>

<script>
    import g_signin_btn from './g-signin-btn.vue'
    import axios from 'axios'

    export default {
        props: ['logged_in'],
        data: function () {
            return {
            username: ''
            }
        },
        components: {
            g_signin_btn       
        },
        methods: {
            sign_in: function (user) {
                var profile = user.getBasicProfile();
                var id_token = user.getAuthResponse().id_token;
                this.name = profile.getGivenName();

                axios.post('http://localhost:5000/api/login', {
                        profile: user.getBasicProfile(),
                        token: id_token
                },{
                    withCredentials: true
                }).then(response => {
                    this.$emit('user_login_state', true);
                }).catch(error => {
                    console.log(error);
                });
            },
            sign_out: function () {
                this.$emit('user_login_state', false);
                var auth2 = gapi.auth2.getAuthInstance();
                auth2.signOut();
            }
        }
    }
</script>
