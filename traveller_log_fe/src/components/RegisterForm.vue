<script setup>
import {ref} from "vue";
import {registerAttempt} from "../apicalls/userCalls.js"


const username = ref("");
const password = ref("");
const password2 = ref("");

const submitSignUp = async (e) => {
    // take the inputs, validate, wrap in a proper json, 

    // todo check if password1 and 2 match

    // send to backend and handle its response by updating 
    let signupResult = await registerAttempt({
        username: username.value, 
        password: password.value
    })
    // app state hopefully with credentials.
    // preferably not do all in this block.
    console.log(signupResult)
    console.log(e)
    console.log(username.value)
    console.log(password.value)
    // if signup was successful, navigate to login page?
    // if it wasn't, show message
}
</script>

<template>

    <form @submit.prevent="submitSignUp">
        <h3>well met, traveller... what be your name?</h3>
        <label for="usernameInput">Username</label>
        <input 
            id="usernameInput"
            type="text"
            required
            autocomplete="username"
            v-model="username"
        />

        <label for="passwordInput">Password</label>
        <input 
            id="passwordInput"
            type="password"
            required
            minlength="8"
            autocomplete="current-password"
            v-model="password"
        />

        <label for="passwordInput2">Password</label>
        <input 
            id="passwordInput2"
            type="password"
            required
            minlength="8"
            autocomplete="current-password"
            v-model="password2"
        />

        

        <button type="submit">Submit</button>
    </form>

</template>