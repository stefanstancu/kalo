<template>
    <div ref='signinBtn' class='btn-sign-in'>Sign In</div>
</template>

<style scoped>
    .btn-sign-in {
          background: #fff;
          font: 16px/22px Roboto;
          padding: 4px 8px;
          border: 1px solid #ccc;
          display: inline-block;
          cursor: pointer;
    }
</style>

<script>
    export default {
        data: function () {
            return {
            }
        },
        mounted() {
            window.gapi.load('auth2', () => {
                const auth2 = window.gapi.auth2.init({
                  client_id: '1012179851696-fkknaicl6dg4g7cplk005v5desvddovj.apps.googleusercontent.com',
                  cookiepolicy: 'single_host_origin'
                });
                auth2.attachClickHandler(this.$refs.signinBtn, {}, googleUser => {
                   this.$emit('done_g_signin', googleUser);
                }, error => console.log(error));
            });
        }
    }
</script>
