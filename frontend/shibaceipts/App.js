import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'
import Receipts from './screens/Receipts'
import ReceiptScanner from './screens/ReceiptScanner'
import CustomDrawerContent from './screens/Drawer'
import ViewShibaceipt from './screens/ViewShibaceipt'
import MyShibaceipts from './screens/MyShibaceipts'

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator drawerContent={(props) => <CustomDrawerContent {...props} />}>
        <Drawer.Screen
          name='Recent Shibaceipts'
          component={Home}
          options={{
            drawerLabel: 'Home',
          }}
        />
        <Drawer.Screen
          name='Receipts'
          component={Receipts}
          options={{
            drawerLabel: 'Receipts',
          }}
        />
        <Drawer.Screen
          name='Receipt Scanner'
          component={ReceiptScanner}
          options={{
            drawerLabel: 'Receipt Scanner',
          }}
        />
        <Drawer.Screen
          name='My Shibaceipts'
          component={MyShibaceipts}
          options={{
            drawerLabel: 'My Shibaceipts',
          }}
        />
        <Drawer.Screen
          name='View Shibaceipt'
          component={ViewShibaceipt}
          options={{
            drawerLabel: '',
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

