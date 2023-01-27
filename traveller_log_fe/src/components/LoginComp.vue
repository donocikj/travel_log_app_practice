<script setup>
//
import { useCredStore } from '../stores/cred.js'

const creds = useCredStore()
console.log(creds.username || "nothing yet")
console.log(creds)

const logoutButtonPush = async () => {
    // call the logout method
    let msg = await creds.logout()
    console.log(msg)

    // navigate to intro view

}


</script>


<template>
    <div>this is a login component</div>
    <!-- if logged in: hello {user} / sign out -->
    <div v-if="creds.username">
        hello {{ creds.username }}
        <div>
            <button @click="logoutButtonPush">Logout</button>
        </div>
    </div>

    <!-- if not logged in: sign in / sign up -->
    <div v-else>
        <div>
            <RouterLink to="/login">Sign In</RouterLink>
        </div>
        <div>
            <RouterLink to="/register">Sign Up</RouterLink>
        </div>
    </div>

</template>

<style>
</style>