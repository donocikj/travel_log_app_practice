<script setup>
import {ref} from "vue";
import {loginAttempt} from "../apicalls/userCalls.js"


const username = ref("");
const password = ref("");
const password2 = ref("");

const submitLogin = async (e) => {
    // take the inputs, validate, wrap in a proper json, 
    // send to backend and handle its response by updating 
    loginAttempt({
        username: username.value, 
        password: password.value
    })
    // app state hopefully with credentials.
    // preferably not do all in this block.
    console.log(e)
    console.log(username.value)
    console.log(password.value)
    // if login was successful, navigate to default view?
    // if it wasn't, show message
}
</script>

<template>

    <form @submit.prevent="submitLogin">
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