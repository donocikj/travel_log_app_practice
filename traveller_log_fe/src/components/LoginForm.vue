<script setup>
import {ref} from "vue";
import { useRouter } from "vue-router";

import { loginAttempt } from "../apicalls/authCalls.js";
import { useCredStore } from "../stores/cred.js";


const creds = useCredStore();
const router = useRouter();

const form_username = ref("");
const form_password = ref("");

const submitLogin = async (e) => {
    // take the inputs, validate, wrap in a proper json, 
    // send to backend and handle its response by updating 
    
    await creds.login({
        username: form_username.value,
        password: form_password.value
    })

    // if login was successful, navigate to default view?
    // if it wasn't, show message
    if(creds.userId) {
        router.push({name:"home"})
    }


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
            v-model="form_username"
        />

        <label for="passwordInput">Password</label>
        <input 
            id="passwordInput"
            type="password"
            required
            minlength="8"
            autocomplete="current-password"
            v-model="form_password"
        />

        <button type="submit">Submit</button>
    </form>
    <div v-if="creds.problem">
        <strong>
            {{creds.problem}}
        </strong>
    </div>

</template>