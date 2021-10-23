import React from 'react'
import { FlatList } from 'react-native'
import { NativeBaseProvider, Thumbnail, ListItem } from 'native-base'
import {MockPosts} from '../mock_backend'

const renderItem = (item) => {
  return (
      <p>{JSON.stringify(item)}</p>
  )
}

export default function Home() {
  console.log(MockPosts)
  return (
    <NativeBaseProvider>
      <FlatList
        data={MockPosts}
        keyExtractor={(item) => item.shibaceipt}
        renderItem={({ item }) => renderItem(item)}
      />
    </NativeBaseProvider>
  )
  return (
    <NativeBaseProvider>
      <View style={{ justifyContent: 'flex-start' }}>
        <FlatList
          data={MockPosts}
          renderItem={({ item }) => (
            <Card>
              <CardItem>
                <Left>
                  <Thumbnail source={item.user.avatar} />
                  <Body>
                    <Text>Kofi</Text>
                    <Text note>26 Feb 2018</Text>
                  </Body>
                </Left>
              </CardItem>
              <CardItem cardBody>
                <Image source={item.shibaceipt} style={{ height: 200, width: null, flex: 1 }} />
              </CardItem>
              <CardItem style={{ height: 45 }}>
                <Left>
                  <Button transparent>
                    <Icon name='ios-heart-outline' style={{ color: 'black' }} />
                  </Button>
                  <Button transparent>
                    <Icon name='ios-chatbubbles-outline' style={{ color: 'black' }} />
                  </Button>
                  <Button transparent>
                    <Icon name='ios-send-outline' style={{ color: 'black' }} />
                  </Button>
                </Left>
              </CardItem>
              <CardItem style={{ height: 20 }}>
                <Text>lol</Text>
              </CardItem>
              <CardItem>
                <Body>
                  <Text>
                    <Text style={{ fontWeight: '800' }}>kofi </Text>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Asperiores soluta dolor eveniet fugiat rem ullam laudantium, quod accusamus autem numquam maxime tempora nisi commodi unde. Nisi repudiandae culpa omnis doloremque!
                  </Text>
                </Body>
              </CardItem>
            </Card>
          )}
        />
      </View>
    </NativeBaseProvider>
  )
}
