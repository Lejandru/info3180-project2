<template>
 	<div class="Car container">
    	<h2>Add New Car</h2>
    	<NewCarForm />
  	</div>
</template>

<script>
import NewCarForm from '@/components/NewCarForm.vue'
export default {

    data() {
        return {};
    },
	components: { NewCarForm }
};
</script>