<template>
 	<div class="Register container">
    	<h2>Registration</h2>
    	<RegistrationForm />
  	</div>
</template>

<script>
import RegistrationForm from '@/components/RegistrationForm.vue'
export default {
    data() {
        return {};
    },
	components: { RegistrationForm }
};
</script>