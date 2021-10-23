import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'
import ReceiptScanner from './screens/ReceiptScanner'
import CustomDrawerContent from './screens/Drawer'

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator drawerContent={(props) => <CustomDrawerContent {...props} />} >
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
            drawerLabel: 'ReceiptScanner',
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

