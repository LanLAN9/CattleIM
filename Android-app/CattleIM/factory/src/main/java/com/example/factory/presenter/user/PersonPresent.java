package com.example.factory.presenter.user;

import com.example.factory.presenter.BasePresenter;
import com.example.netKit.NetKit;
import com.example.netKit.db.User;

public class PersonPresent extends BasePresenter<PersonContract.View>
        implements PersonContract.Presenter {


    public PersonPresent(PersonContract.View view) {
        super(view);
    }

    @Override
    public void start() {
        NetKit.runOnAsync(new Runnable() {
            @Override
            public void run() {
                PersonContract.View view = getView();
                if (view != null){
                    final String userId = getView().getUserId();
                    User info = UserHelper.getInfo(userId);
                    onLoad(info);
                }

            }
        });
    }

    private void onLoad(User info) {


    }

    @Override
    public void destroy() {

    }


}
