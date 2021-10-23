import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'
import ReceiptScanner from './screens/ReceiptScanner'

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen
          name='Recent Shibaceipts'
          component={Home}
          options={{
            drawerLabel: 'Home',
          }}
        />
        <Drawer.Screen
          name='ReceiptScanner'
          component={ReceiptScanner}
          options={{
            drawerLabel: 'ReceiptScanner'
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

