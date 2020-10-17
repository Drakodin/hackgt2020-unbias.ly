import React from 'react';
import { Grid, Card, CardContent, CardActions, CardMedia } from '@material-ui/core'
import { getNews } from './news-fetch/news-endpoint';

export default class NewsDisplay extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            /*
            Article JSON
            {
                provider: String
                title: String
                rank: Number
            }
            */
            articles: [],
            loading: false
        }
    }

    componentDidMount() {
        this.setState({loading: true});
        getNews().then(data => this.setState({articles: data.data},
            () => {
                this.setState({loading: false})
            }
        ));
    }

    parseLink = (link) => {
        let hostname = (new URL(link)).hostname;
        return hostname.substring(hostname.indexOf('.') + 1, hostname.lastIndexOf('.'));
    }

    render() {
        if (!this.state.loading) {
            return (
                <>
                    <Grid item container direction="column" spacing={3} xs={8}>
                        {this.state.articles.map(v => (
                            <Card key={v.link}>
                                <CardContent>
                                    <h1>{this.parseLink(v.link)}</h1>
                                    <p>{v.score}</p>
                                </CardContent>
                            </Card>
                        ))}
                    </Grid>
                </>
            )
        } else {
            return <p>Please Wait...</p>
        }
    }
}