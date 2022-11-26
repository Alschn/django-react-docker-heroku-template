// it is not possible to pass API URL as env variable intp heroku's docker container
export const API_URL = import.meta.env.DEV ? 'http://localhost:8000' : '';
