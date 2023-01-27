import {useCredStore} from "../stores/cred.js"

// todo move to some ini or env
const hostname = location.hostname
const port = 8000

export function loginAttempt(creds) {
    console.log(`calling:`)
    console.log(`http://${hostname}:${port}/auth/login/`)
    return fetch(`http://${hostname}:${port}/auth/login/`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            "content-type":"application/json",
        },
        body: JSON.stringify({
            username: creds.username,
            password: creds.password,
        })
    })
        .then(async (res)=>{
            // test for status of response

            // update creds in state?
            useCredStore().username = creds.username
            // return creds
        })
        .catch(err => {
            // handle errors
        })

}


export function credRetrievalAttempt() {
    console.log('calling')
    console.log(`http://${hostname}:${port}/auth/`)
    return fetch(`http://${hostname}:${port}/auth/`, {
        method: 'GET',
        credentials: 'include'
    })
        .then(async (res) => {
            // test response status
            console.log(res)
            return res.json()
        })
        .then((data) => {
            // assign retrieved creds to store
            console.log(data)
            // credStore = useCredStore()
            // credStore.username = data.username
            // credStore.userId = data.id
            // console.log(credStore)
            return data
        })
        .catch((err) => {
            // something went wrong
        })
}

export function logoutCall() {
    console.log('calling')
    console.log(`http://${hostname}:${port}/auth/logout`)
    return fetch(`http://${hostname}:${port}/auth/logout`, {
        method: 'GET',
        credentials: 'include'
    })
        .then(async (res) => {
            // test response status
            console.log(res)
            return res.json()
        })
        .then((data) => {
            // assign retrieved creds to store
            console.log(data)
            // credStore = useCredStore()
            // credStore.username = data.username
            // credStore.userId = data.id
            // console.log(credStore)
            return data
        })
        .catch((err) => {
            // something went wrong
        })
}