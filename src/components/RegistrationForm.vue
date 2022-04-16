<template>
  <div id="app">
    <form @submit.prevent="login">
        <div class="form-group">
        <label>Username</label>
        <input type="text" class="form-control form-control-lg"/>
        </div>
      
        <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control form-control-lg"/>
        </div>

        <div class="form-group">
        <label>Name</label>
        <input type="text" class="form-control form-control-lg"/>
        </div>

        <div class="form-group">
        <label>Email</label>
        <input type="email" class="form-control form-control-lg"/>
        </div>

        <div class="form-group">
        <label>Location</label>
        <input type="text" class="form-control form-control-lg"/>
        </div>

      <div>
        <label for="Biography">Biography</label><br>
        <textarea name="Biography" class="form-control"></textarea>
      </div>

      <div>
        <label for="photo"> Photo Upload </label><br>
        <input type="file" name="photo" class="form-control" id="photo"><br>
      </div>

     <button type="submit" class="btn btn-dark btn-lg btn-block">Register</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "RegistrationForm",
  data() {
    return {
      username: "",
      Password: "",
      Name: "",
      Email: "",
      Location: "",
      Biography: "",
      address: ""
    };
  },
  methods: {
    async login() {
      const { username, Password, Name, Email, Location,  Biography, address } = this;
      const res = await fetch(
        
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username,
            Password,
            Name,
            Email,
            Location,
            Biography,
            address
          })
        }
      );
      const data = await res.json();
      console.log(data);
    }
  }
};
</script>