import React from 'react';
import { Grid, Card, CardContent, CardActions, CardMedia } from '@material-ui/core'
import { getNews } from './news-fetch/news-endpoint';

class NewsDisplay extends React.Component {
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
            articles = [],
            loading = false
        }
    }

    componentDidMount() {
        this.setState({loading: true});
        getNews().then(data => this.setState({articles: data},
            () => {
                this.setState({loading: false})
            }
        ));
    }

    render() {
        if (!this.state.loading) {
            return (
                <>
                    <Grid item container direction="column" spacing={3}>
                        {this.state.articles.map(v => (
                            <Card key={v.title}>
                                <CardContent>

                                </CardContent>
                            </Card>
                        ))}
                    </Grid>
                </>
            )
        }
    }
}