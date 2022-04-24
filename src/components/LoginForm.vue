<template>
    <form @submit.prevent="userLogin" method="POST" enctype="multipart/form-data" id="loginForm">
        
        <label>Username</label>
        <input type="username" id="username" class="form-control form-control-lg"/>
        
        <label>Password</label>
        <input type="password" id="password" class="form-control form-control-lg"/>

        <button type="submit">Login</button>
    </form>
</template>


<script>
export default {
    name: 'loginForm',
    data(){
        return {
            message: 'Login successful!'
        }
    },
    methods: {
        userLogin(){
            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);
            let self = this
            fetch("/api/auth/login",{
                method: 'POST',
                body: form_data,
                headers:{
                    Accept:'application/json',
            }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
        }
    }
}
</script>