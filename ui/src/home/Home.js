import React from 'react';
import { Button } from '@material-ui/core';
import { preload } from './init';

const Home = () => {
    const [connected, setConnected] = React.useState(false);

    const begin = () => {
        preload().then(data => setConnected(data.connected))
    }

    if (connected) {
        window.location.href = `/news`;
    }

    return (
        <>
            <h1>Hi</h1>
            <Button onClick={begin}>
                Go To the News
            </Button>
        </>
    )
}

export default Home;