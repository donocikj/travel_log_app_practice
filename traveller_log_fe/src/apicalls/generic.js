



export async function apiCall(url, fetchOptions) {
    // console.log(`calling url: ${url}`)
    
    return fetch(url, fetchOptions)
        .then(async (res)=>{
            // test for status of response
            if(res.ok) {
                // console.log("returning res:")
                // console.log(res)
                return res.json()
            }
            // this is probably not a good idea since it lets the fe relay messages returned from BE instead of interpreting them...
            let responseObject = await res.json()
            return {err: responseObject.message}
        })
        // .then((data)=>{
        //     return data
        // })
        .catch(err => {
            // handle errors
        })

}