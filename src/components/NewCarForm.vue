<template>
    <form method="POST" enctype="multipart/form-data" id="NewCarForm">
     
        <label>Make</label>
        <input type="make" id="make" class="form-control form-control-lg"/><br>
    
      
      
        <label>Model</label>
        <input type="model" id="model" class="form-control form-control-lg"/><br>
    

       
        <label>Colour</label>
        <input type="colour" id="colour" class="form-control form-control-lg"/><br>
     

       
        <label>Price</label>
        <input type="price" id="price" class="form-control form-control-lg"/><br>
       

   
        <label>Car Type</label>
        <select type="car_type" id ="car_type" class="form-control form-control-lg">

        <option value="SUV">SUV</option>
        <option value="Sedan">Sedan</option>
        <option value="Coupe">Coupe</option>
        <option value="Wagon">Wagon</option>
        <option value="Convertible">Convertible</option>
        </select><br>



        <label>Transmission</label>
        <select type="transmission" id ="transmission" class="form-control form-control-lg">

        <option value="Automatic">Automatic</option>
        <option value="Manual">Manual</option>
        </select><br>
   

    
        <label for="Description">Description</label><br>
        <textarea name="description" id="description" class="form-control"></textarea>
 

    
        <label for="photo"> Upload Photo </label><br>
        <input type="file" name="photo" class="form-control" id="photo"><br>
      

     <button type="submit" class="btn btn-dark btn-lg btn-block">Save</button>

    </form>
  
</template>

<script>
export default {
  name: "NewCarForm",

}
</script>