import { ref } from 'vue'
import { defineStore } from 'pinia'
import { credRetrievalAttempt, loginAttempt, logoutCall } from '../apicalls/userCalls'

export const useCredStore = defineStore({
    id: 'cred', 
    state: () => ({
        username: ref(""),
        userId: ref(0),
    }),

    getters: {
        // return creds
    },
    actions: {
        // refresh creds
        async authAttempt() {
            let receivedCreds = await credRetrievalAttempt()
            if (receivedCreds) {
                this.username = receivedCreds.username
                this.userId = receivedCreds.id
            }
            return {msg: "Auth attempt"}
        },
        // login

        async login(creds) {
            // make the call
            let loginResult = await loginAttempt(creds)

            // deal with failure (ensure login is available)
            if(!loginResult) {
                this.username = ""
                this.userId = 0
            }
            // deal with success (update user id and username)
            else {
                console.log(loginResult)
                this.username = loginResult.welcome
                this.userId = loginResult.id
            }

            return {msg: `login attempt with ${creds.username}, ${creds.password}`}
        },

        // logout
        async logout() {
            // make the call
            let msg = await logoutCall()
            // clear username and id, make sure login is available
            this.username = ""
            this.userId = 0

            return msg 
        },
        // sign up

        async signUp(creds) {
            // make the call

            // deal with failure (show appropriate msg)

            // prompt login (nav to login view)
        }
    }
    
})
    

