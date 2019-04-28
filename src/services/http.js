import axios from 'axios'

const http = axios.create({
    baseURL: process.env.API_URL
})
export const fetchTrendingTopics = regionId => http.get(`/api_example/topics/${regionId}/`)
export const fetchTwettsSearch = query => http.get(`/api_example/search/${query}/`)

// }).catch((err) => {
//     console.error(err);
//     alert(`Houve um erro ao carregar dados(${err.status.code}): `)
// });