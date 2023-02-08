import { apiCall } from "./generic";

// todo move to some ini or env
const hostname = location.hostname
const port = 8000

export function getTravels(offset, pageSize, filters) {
    

    let result = apiCall(
        `http://${hostname}:${port}/tlog/travels/`,
        {
            method: 'GET',
            credentials: 'include',
        }
    );

    return result
}