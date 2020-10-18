export const preload = () => {
    return fetch(`/api/boot`, 
    {
        method: 'GET',
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }).then(res => {
        return res.json()
    }).catch(err => console.error(err)) 
}