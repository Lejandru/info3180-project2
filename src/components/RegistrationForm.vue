<template>
    <form @submit.prevent="registerUser" method="POST" enctype="multipart/form-data" id="registerForm">
     
        <label>Username</label>
        <input type="username" id="username" class="form-control form-control-lg"/>
    
      
      
        <label>Password</label>
        <input type="password" id="password" class="form-control form-control-lg"/>
    

       
        <label>Name</label>
        <input type="text" id="name" class="form-control form-control-lg"/>
     

       
        <label>Email</label>
        <input type="email" id="email" class="form-control form-control-lg"/>
       

   
        <label>Location</label>
        <input type="text" id="location" class="form-control form-control-lg"/>
   

    
        <label for="Biography">Biography</label><br>
        <textarea name="Biography" id="bio" class="form-control"></textarea>
 

    
        <label for="photo"> Photo Upload </label><br>
        <input type="file" name="photo" class="form-control" id="photo"><br>
      

     <button type="submit" class="btn btn-dark btn-lg btn-block">Register</button>

    </form>
  
</template>

<script>
export default {
  name: "registerForm",
  data() {
    return {
      message: 'Registration successful!'
    }
  },
  methods: {
    registerUser(){
      let registerForm = document.getElementById('registerForm');
      let form_data = new FormData(registerForm);
      let self = this
      fetch("/api/register",{
        method: 'POST',
        body: form_data
      })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
                
        console.log(data);
      })
   
    }
  }
}
</script>