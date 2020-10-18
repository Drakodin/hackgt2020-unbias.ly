import React from 'react';
import { Grid, Card, CardContent, CardActionArea, Collapse, IconButton, CardActions } from '@material-ui/core'
import { Typography, Box, Divider } from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { getNews } from './news-fetch/news-endpoint';

export default class NewsDisplay extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            /*
            Article JSON
            {
                link: String
                score: Number
                title: Title
            }
            */
            articles: [],
            expanded: false,
            loading: false
        }
    }

    componentDidMount() {
        this.setState({loading: true});
        // Get news from DB, parsing out bad scrapes
        getNews().then(data => {
            data.data.sort((a, b) => parseFloat(a.score) - parseFloat(b.score));
            data.data.filter(v => (v.link !== "https://www.ndtv.com/education" || v.link !== "https://www.ndtv.com/tamil-nadu-news"))
            this.setState({articles: data.data}, () => this.setState({loading: false}))
        });
    }

    parseLink = (link) => {
        let hostname = (new URL(link)).hostname;
        return hostname.substring(hostname.indexOf('.') + 1, hostname.lastIndexOf('.'));
    }

    render() {
        if (!this.state.loading) {
            return (
                <>
                    <Grid style={{backgroundColor: '#4c8bf5'}} alignItems="center" item container xs={12}>
                        <Grid item container direction="column" justify="center" alignItems="center" alignContent="center" spacing={3} xs={9} style={{margin: 3}}>
                            <Grid item container xs={12} style={{margin: 3}}>
                                <Grid container direction="column">
                                    <Typography variant="h3" style={{color: 'white'}}>Unbias.ly</Typography>
                                    <Typography variant="body1" style={{color: 'white'}}>The News!</Typography>
                                </Grid>
                                <Box>
                                    <Divider/>
                                </Box>
                            </Grid>
                            {this.state.articles.map((v, i) => {
                                return (
                                    <Card key={v.link} style={{margin: 10, maxWidth: '85%'}} elevation={4}>
                                        <CardActionArea onClick={() => window.open(v.link, '_blank')}>
                                            <CardContent>
                                                <h1>{v.title}</h1>
                                                <p>{v.score}</p>
                                            </CardContent>
                                            <CardContent>
                                                <Typography paragraph>
                                                    {v.summary}
                                                </Typography>
                                            </CardContent>
                                        </CardActionArea>
                                    </Card>
                                )
                            })}
                        </Grid>
                    </Grid>
                </>
            )
        } else {
            return <p>Please Wait...</p>
        }
    }
}