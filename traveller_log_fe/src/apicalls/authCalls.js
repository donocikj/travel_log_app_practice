import { apiCall } from "./generic.js"

// todo move to some ini or env
const hostname = location.hostname
const port = 8000

// 
export function loginAttempt(creds) {

    return apiCall(
        `http://${hostname}:${port}/auth/login/`,
        {
            method: 'POST',
            credentials: 'include',
            headers: {
                "content-type":"application/json",
            },
            body: JSON.stringify({
                username: creds.username,
                password: creds.password,
            })
        });

    // TODO - handle the varying paths to failure

}

export function credRetrievalAttempt() {

    return apiCall(
        `http://${hostname}:${port}/auth/`,
        {
            method: 'GET',
            credentials: 'include'
        });

}

export function logoutCall() {

    return apiCall(
        `http://${hostname}:${port}/auth/logout`,
        {
            method: 'GET',
            credentials: 'include'
        });

}


export function registerAttempt(creds) {

    return apiCall(
        `http://${hostname}:${port}/auth/users/`,
        {
            method: 'POST',
            credentials: 'include',
            headers: {
                "content-type":"application/json",
            },
            body: JSON.stringify({
                username: creds.username,
                password: creds.password,
            })
        });

}