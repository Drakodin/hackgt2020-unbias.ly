export const getNews = () => {
    return fetch(`/news`, {
        method: "GET",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        }
    }).then(res => {
        if (res.ok) {
            return res.json();
        } else {
            Promise.reject("Response invalid")
        }
    }).catch(err => {
        console.error(err);
    })
}