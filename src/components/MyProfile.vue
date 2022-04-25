<template>

    <div class="flexing">
        <div class="user-favs">
            <div class="user-card">
              <img id="user_img" :src="'/uploads/' + user.photo" alt="A user's image">
                <div class="user-details">
                    <h1>{{user.name}}</h1>
                    <h2 class="grey">@{{user.username}}</h2>
                    <p class="bio">{{user.biography}}</p>
                    <div class="other-info">
                        <div>
                            <p class="grey">Email</p><p>{{user.email}}</p>
                        </div>
                        <div>
                            <p class="grey">Location</p><p>{{user.location}}</p>
                        </div>
                        <div>
                            <p class="grey">Joined</p><p>{{user.date_joined}} </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="favourites">
                <h2>Cars Favourited</h2>
                <div class="car-grid">
                    <div class="fav-car">
                        <img src="../static/images/logo.png" alt="A car">
                        <div class="row">
                            <p>2020 Lamborghini</p>
                            <p class="price">
                                <i class="fas fa-tag"></i>$356,335
                            </p>
                        </div>
                        <p class="grey">Hurrican</p>
                        <a href="#">View more details</a>
                    </div>
                    <div class="fav-car">
                        <img src="../static/images/logo.png" alt="A car">
                        <div class="row">
                            <p>2020 Lamborghini</p>
                            <p class="price">
                                <i class="fas fa-tag"></i>$356,335
                            </p>
                        </div>
                        <p class="grey">Hurrican</p>
                        <a href="#">View more details</a>
                    </div>
                    <div class="fav-car">
                        <img src="../static/images/logo.png" alt="A car">
                        <div class="row">
                            <p>2020 Lamborghini</p>
                            <p class="price">
                                <i class="fas fa-tag"></i>$356,335
                            </p>
                        </div>
                        <p class="grey">Hurrican</p>
                        <a href="#">View more details</a>
                    </div>
                    <div class="fav-car">
                        <img src="../static/images/logo.png" alt="A car">
                        <div class="row">
                            <p>2020 Lamborghini</p>
                            <p class="price">
                                <i class="fas fa-tag"></i>$356,335
                            </p>
                        </div>
                        <p class="grey">Hurrican</p>
                        <a href="#">View more details</a>
                    </div>
                    <div class="fav-car">
                        <img src="../static/images/logo.png" alt="A car">
                        <div class="row">
                            <p>2020 Lamborghini</p>
                            <p class="price">
                                <i class="fas fa-tag"></i>$356,335
                            </p>
                        </div>
                        <p class="grey">Hurrican</p>
                        <a href="#">View more details</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>



export default {
  data() {
            return {
                allcars: [],
                user:{}
            }
         },created: function(){
            let self = this;
            this.viewUserinfo(self.user_id);
            this.carsfavourited(self.user_id);
        },
    
        methods: {
            viewUserinfo(user_id){
                let self = this;
                fetch('/api/users/' + user_id, {
                    method: 'GET',
                    headers:{ 'Authorization': 'Bearer ' + sessionStorage.getItem('token'),'X-CSRFToken': token } 
                   })
                    .then(function (response) {
                    return response.json();
                    })
                    .then(function (jsonResponse) {
                    self.user=jsonResponse.user;
                    })
                    .catch(function (error) {
                    console.log(error);
                    });
    
                },
                carsfavourited: function(user_id){
                    let self = this;
                    fetch("/api/users/" + user_id + "/favourites", { method: 'GET', headers: { 'Authorization': 'Bearer ' + sessionStorage.getItem('token'), 'X-CSRFToken': token }, credentials: 'same-origin'})
                    .then(function (response) {
                        return response.json();
                        }).then(function (jsonResponse) {
                            // display a success message
                            self.allcars=jsonResponse.favouritecars
                            console.log(jsonResponse);
                        }).catch(function (error) {
                                console.log(error);
                            });
                },
                carinfo: function(car_id){ 
                    this.$router.push("/cars/"+car_id)
                   
                },
    
    
            },
            
        }
  
</script>

<style>

*,
::after,
::before {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

.flexing {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f3f4f6;
  padding: 30px 0px;
}

.user-favs,
.other-info,
.favourites,
.make-model {
  display: flex;
  flex-direction: column;
  font-family: sans-serif;
}

.user-favs h1 {
  margin-bottom: 20px;
}

/* User Profile Styles */
.user-card {
  width: 850px;
  display: flex;
  flex-direction: row;
  background-color: #fff;
  border-radius: 10px;
  padding: 15px;
  box-shadow: 0px 3px gray;
  margin-bottom: 30px;
}

.user-card img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: solid 1px grey;
  margin: 10px 30px 0px 10px;
}

.user-details {
  display: grid;
  grid-template-columns: auto;
  grid-template-rows: repeat(4, auto);
}

.bio {
  width: 400px;
  color: #ababb0;
  margin: 20px 0px;
  line-height: 1.5em;
}

/* .other-info {
    display: flex;
    flex-direction: column;
} */

.other-info > div {
  font-weight: bold;
  column-count: 2;
  padding: 5px 0px;
}

/* Cars Favourited Styles */
.car-grid {
  display: grid;
  grid-template-columns: repeat(3, auto);
  grid-template-rows: auto;
  gap: 20px;
}

.favourites h2 {
  font-weight: bold;
  margin-bottom: 5px;
}

.favourites .fav-car {
  display: grid;
  grid-template-columns: auto;
  grid-template-rows: repeat(3, auto);
  max-width: 280px;
  height: fit-content;
  background-color: #fff;
  border-radius: 5px;
}

.fav-car > * {
  padding: 0px 10px;
}

.fav-car img {
  width: 100%;
  height: 200px;
  border-radius: 5px 5px 0px 0px;
  padding: 0px;
}

.favourites .fav-car .row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0px 0px;
  gap: 10px;
}

.row > p {

  word-wrap: normal;
}

.favourites .fav-car .price {
  color: #fff;
  background-color: #41b883;
  padding: 5px 8px;
  border-radius: 10px;
}

.price i {
  padding-right: 5px;
}

.favourites .fav-car > a {
  text-decoration: none;
  color: #fff;
  background-color: #0000ff;
  padding: 10px;
  text-align: center;
  width: 90%;
  border-radius: 10px;
  margin: 50px auto 10px auto;
}

/* Other Styles */
.grey {
  color: #8c8f98;
}

/* Search Section */
.search-car {
  width: 850px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 50px;
}

#search-form {
  width: 100%;
  height: fit-content;
  padding: 40px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  background-color: #fff;
  border-radius: 10px;
}

#search-form fieldset {
  display: flex;
  flex-direction: column;
  border: none;
}

#search-form fieldset > input {
  padding: 10px;
  border: solid 1px grey;
  border-radius: 5px;
  margin-top: 3px;
  width: 300px;
}

#search-form button {
  color: #fff;
  background-color: #41b883;
  padding: 10px 40px;
  border-radius: 8px;
  border: none;
  margin-top: 20px;
  cursor: pointer;
}
</style>